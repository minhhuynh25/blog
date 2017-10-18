from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post


def posts_list(request):
    queryset = Post.objects.all()
    context ={
        "object_list":queryset,
        "title": "List"
    }
    return render(request,"index.html",context)


def posts_create(request):
    context = {
        "title": "Create"
    }
    return HttpResponse("<h1>Create</h1>",context)


def posts_detail(request):
    instance = get_object_or_404(Post, id=2)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request,"detail.html",context)


def posts_update(request):
    context = {
        "title": "Update"
    }
    return HttpResponse("<h1>Update</h1>",context)


def posts_delete(request):
    context = {
        "title": "Delete"
    }
    return HttpResponse("<h1>Delete</h1>",context)

