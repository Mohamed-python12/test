from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def courses(request):
    return render(request, "courses.html")

def social_media(request):
    return render(request, "social medias.html")

def support(request):
    return render(request, "support.html")