from django.shortcuts import render
from apps.portfolio.models import Project

# Create your views here.
def portafolio(request):
    projects= Project.objects.all()

    return render(request, 'portfolio/portfolio1.html', {'projects':projects})
