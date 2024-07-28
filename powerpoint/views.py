from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PowerPoint
from .forms import PowerPointForm

# Check if the user is an admin
def is_admin(user):
    return user.is_superuser

@login_required
def powerpoint_list(request):
    powerpoints = PowerPoint.objects.all()
    return render(request, 'powerpoint/powerpoint_list.html', {'powerpoints': powerpoints})

@user_passes_test(is_admin)
def powerpoint_upload(request):
    if request.method == 'POST':
        form = PowerPointForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('powerpoint_list')
    else:
        form = PowerPointForm()
    return render(request, 'powerpoint/powerpoint_upload.html', {'form': form})

