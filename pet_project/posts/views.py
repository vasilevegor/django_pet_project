from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    template = 'posts/index.html'
    title = 'This is main page of Pet project'
    context = {
        'title': title
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = f'Here you will see info about groups + {slug}'
    context = {
        'title': title
    }
    return render(request, template, context)

