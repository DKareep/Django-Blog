from django.shortcuts import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .forms import PostForm
from models import Post


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get("titlec")
        instance.save()

    # if request.method == 'POST':
    #     print request.POST.get('title')
    #     print request.POST.get('content')
    context = {
        "title": "create",
        "form": form
    }
    return render(request, "form_view.html", context)


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
