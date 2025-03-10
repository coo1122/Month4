from django.shortcuts import render
from django.http import HttpResponse
import random


def test_view(request):
    return HttpResponse(f"Hello world! {random.randint(1,100)}")


def html_view(request):
    return render(request, "posts/test.html")
