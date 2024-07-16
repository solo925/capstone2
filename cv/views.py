from django.shortcuts import render
from .models import CV

def cv_view(request):
    cvs = CV.objects.all()
    context = {'cvs': cvs}
    return render(request, 'cv/cv.html', context)
