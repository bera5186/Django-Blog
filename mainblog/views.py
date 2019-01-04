from django.shortcuts import render
from . models import Post

def index(request):
    context = {
        'post': Post.objects.all()

    }
    return render(request, 'mainblog/index.html', context=context)

def about(request):
    return render(request, 'mainblog/about.html', {'title':'about page'})

