from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request, "home.html")

def aboutMe(request):
    return render(request, "about_me.html")

def educationPage(request):
    return render(request, "education.html")

def contactPage(request):
    context = {}
    if request.method == 'POST':
        context["thank_you"] = "Thank you for reaching out! I will get back to you soon."
        return render(request, "contact.html", context)
    return render(request, "contact.html")
