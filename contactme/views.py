from django.shortcuts import render

# Create your views here.
def showcontactme(request):
    return render(request, 'contactme/contactmepage.html')
