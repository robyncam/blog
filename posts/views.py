from django.shortcuts import render
from posts.models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    #get all of the objects from the database Posts
    return render(request, 'index.html', {'posts': posts})
