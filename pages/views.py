from django.shortcuts import render
from listings.models import Listing

# Create your views here.

def index(request):
    listings = Listing.objects.all()
    content = {"listings":listings}
    return render(request, 'pages/index.html', content)

def about(request):
    return render(request, 'pages/about.html')

