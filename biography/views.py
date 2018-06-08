from django.shortcuts import render
from .models import Favbooks
from .models import Favmovies
# Create your views here.
def showbiography(request):
    books = Favbooks.objects
    movies = Favmovies.objects
    return render(request,'biography/biographypage.html',{'books':books,'movies':movies})
