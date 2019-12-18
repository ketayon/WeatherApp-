from django.shortcuts import render
from .models import Bb

# Create your views here.

def landing(request):
    bbs = Bb.objects.all()
    return render(request, 'landing/landing.html', {'bbs': bbs})