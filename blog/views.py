from django.shortcuts import render
from .models import Blog

def allblog(request):
    return render(request,'blog/allblog.html')
