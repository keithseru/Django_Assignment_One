from django.shortcuts import render

# Create your views here.

def aboutMe(request):
    return render(request, "about_me.html")

def educationPage(request):
    return render(request, "education.html")

def contactPage(request):
    return render(request, "contact.html")
