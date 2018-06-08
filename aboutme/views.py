from django.shortcuts import render
from .models import Aboutme
# Create your views here.
def aboutme(request):
    descriptions = Aboutme.objects
    return render(request,'aboutme/aboutmepage.html',{'descriptions':descriptions})
