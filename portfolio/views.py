from django.shortcuts import render
from .models import Projects
# Create your views here.
def showportfolio(request):
    projects = Projects.objects
    return render(request,'portfolio/portfoliopage.html',{'projects':projects})
