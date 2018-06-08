from django.shortcuts import render
from .models import Skills
# Create your views here.
def showhireme(request):
    skills = Skills.objects
    return render(request,'hireme/hiremepage.html',{'skills':skills})
