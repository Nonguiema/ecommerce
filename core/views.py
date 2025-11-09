from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about(request):
    """Page À propos."""
    return render(request, 'core/about.html')

def contact(request):
    """Page Nous contacter."""
    return render(request, 'core/contact.html')

