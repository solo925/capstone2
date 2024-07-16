from django.shortcuts import render
from .models import Video

def videos_view(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'videos/video.html', context)
