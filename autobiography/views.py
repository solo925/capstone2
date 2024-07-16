from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Autobiography
from .forms import AutobiographyForm

# Check if the user is an admin
def is_admin(user):
    return user.is_superuser

def autobiography_list(request):
    autobiographies = Autobiography.objects.all()
    return render(request, 'autobiography/autobiography_list.html', {'autobiographies': autobiographies})

@user_passes_test(is_admin)
def autobiography_create(request):
    if request.method == 'POST':
        form = AutobiographyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('autobiography_list')
    else:
        form = AutobiographyForm()
    return render(request, 'autobiography/autobiography_form.html', {'form': form})

def autobiography_detail(request, pk):
    autobiography = get_object_or_404(Autobiography, pk=pk)
    return render(request, 'autobiography/autobiography_detail.html', {'autobiography': autobiography})



