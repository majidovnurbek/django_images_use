from django.shortcuts import render
from .models import Posts

def index(request):
    posts = Posts.objects.all()
    return render(request, 'list.html', {'posts': posts})