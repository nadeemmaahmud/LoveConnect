from django.shortcuts import render

def landing_page(request):
    """Landing page for the dating website"""
    return render(request, 'main/landing.html')
