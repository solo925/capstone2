from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Video
from .forms import VideoForm

@login_required
def videos_view(request):
    form = None
    if request.user.is_superuser:
        if request.method == 'POST':
            form = VideoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('videos_view')
        else:
            form = VideoForm()
    videos = Video.objects.all()
    context = {'videos': videos, 'form': form}
    return render(request, 'videos/video.html', context)
