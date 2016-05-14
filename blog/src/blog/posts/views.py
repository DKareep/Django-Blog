from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.

def post_create(request):
    return render(request, "index.html")

def post_detail(request):
    return HttpResponse("<h1>Detail</h1>")

def post_list(request):
    return HttpResponse("<h1>List</h1>")

def post_update(request):
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")

