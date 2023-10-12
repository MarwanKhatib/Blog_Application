from django.shortcuts import render, get_object_or_404
from django.http import Http404
from . import models

# Create your views here.


def posts_list(request):
    posts = models.Post.objects.all()
    return render(request, "blog/post/list.html", {"posts": posts})


def post_details(request, year, month, day, post):
    # Method 2
    post = get_object_or_404(
        models.Post,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        status=models.Post.Status.PUBLISHED,
    )
    return render(request, "blog/post/details.html", {"post": post})
