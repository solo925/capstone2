from django.shortcuts import render

from django.shortcuts import render
# from . models import Profile

def home_view(request):
    # pic = Profile.objects.all()
    
    context = {
        'title': 'Welcome to My Website',
        'subtitle': 'Capstone Project',
        'description': 'Hello, I am a passionate software engineer dedicated to creating efficient and user-friendly applications.',
        'image_url': 'media/profile_photo/wp5022349_9ETab0W.jpg' # Update with your actual photo URL
    }
    return render(request, 'core/home.html', context)


    
    


