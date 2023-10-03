from django.shortcuts import render, get_object_or_404
from django.http import Http404
from . import models

# Create your views here.


def posts_list(request):
    posts = models.Post.objects.all()
    return render(request, "blog/post/list.html", {"posts": posts})


def post_details(request, id):
    # Method 1
    # try:
    #     posts = models.Post.objects.get(id=id)
    # except models.Post.DoesNotExist:
    #     raise Http404("No Posts Found")
    # return render(request, "blog/post/details.html", {"posts": posts})

    # Method 2
    post = get_object_or_404(models.Post, id=id, status=models.Post.Status.PUBLISHED)
    return render(request, "blog/post/details.html", {"post": post})
