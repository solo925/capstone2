from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Video

@login_required
def videos_view(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'videos/video.html', context)
