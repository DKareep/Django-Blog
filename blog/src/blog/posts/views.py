from django.shortcuts import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.

from models import Post


def post_create(request):
    context = {
        "title": "create"
    }
    return render(request, "index.html", context)


def post_detail(request, id):
    # instance = Post.objects.get(id = 30)
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, "detail_view.html", context)


def post_list(request):
    queryset = Post.objects.all()
    if request.user.is_authenticated():
        context = {
            "object_list": queryset,
            "title": "list new"
        }
    else:
        context = {
            "title": "list"
        }
    return render(request, "index.html", context)


def post_update(request):
    return HttpResponse("<h1>Update</h1>")


def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
