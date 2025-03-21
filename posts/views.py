from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from posts.models import Post
from posts.forms import PostCreateform, PostCreateform2


def test_view(request):
    return HttpResponse(f"Hello world! {random.randint(1,100)}")


def home_page_view(request):
    if request.method == "GET":
        return render(request, "base.html")

def post_list_view(request):
    posts = Post.objects.all()
    if request.method == "GET":
        return render(request, "posts/post_list.html", context={"posts": posts})


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "posts/post_detail.html", context={"post": post})


def post_create_view(request):
    if request.method == "GET":
        form = PostCreateform2()
        return render(request, "posts/post_create.html", context={"form": form})
    if request.method == "POST":
        form = PostCreateform2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "posts/post_create.html", context={"form": form})
        elif form.is_valid():
            form.save()
            # title = form.cleaned_data.get("title")
            # content = form.cleaned_data.get("content")
            # image = form.cleaned_data.get("image")
            # post = Post.objects.create(title=title, content=content, image=image)
        # if post:
            return redirect("/posts/")