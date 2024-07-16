from django.shortcuts import render, get_object_or_404
from .models import Contact
# from .forms import ContactForm
from django.contrib.auth.decorators import user_passes_test

def contact_view(request):
    contact = Contact.objects.first()  # Assuming there is only one contact entry
    return render(request, 'contacts/contact.html', {'contact': contact})

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def contact_edit(request):
    contact = Contact.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_view')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_edit.html', {'form': form})
