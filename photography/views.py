from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import PhotoEssay
from .forms import PhotoEssayForm

# Check if the user is an admin
def is_admin(user):
    return user.is_superuser

def photo_essay_list(request):
    photo_essays = PhotoEssay.objects.all()
    return render(request, 'photography/photo_essay_list.html', {'photo_essays': photo_essays})

@user_passes_test(is_admin)
def photo_essay_create(request):
    if request.method == 'POST':
        form = PhotoEssayForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_essay_list')
    else:
        form = PhotoEssayForm()
    return render(request, 'photography/photo_essay_form.html', {'form': form})

def photo_essay_detail(request, pk):
    photo_essay = get_object_or_404(PhotoEssay, pk=pk)
    return render(request, 'photography/photo_essay_detail.html', {'photo_essay': photo_essay})
