from django.shortcuts import render, get_object_or_404
from django.http import Http404
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST

# def posts_list(request):
#     posts = models.Post.objects.all()
#     paginator = Paginator(posts, 3)
#     page_number = request.GET.get("page", 1)
#     try:
#         posts = paginator.page(page_number)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     return render(request, "blog/post/list.html", {"posts": posts})


class PostListView(ListView):
    """
    Alternative Post List View
    """

    model = models.Post
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"


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
    comments = post.comments.filter(active=True)
    form = CommentForm()
    return render(
        request,
        "blog/post/details.html",
        {"post": post, "comments": comments, "form": form},
    )


def post_share(request, id):
    post = get_object_or_404(models.Post, id=id, status=models.Post.Status.PUBLISHED)
    sent = False
    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} Recommends you read {post.title}"
            message = f"Read {post.title} at {post_url} \n {cd['name']} 's comments: {cd['comments']}"
            send_mail(subject, message, "marwanalkhatibeh@gmail.com", [cd["to"]])
            sent = True
    else:
        form = EmailPostForm()
    return render(
        request, "blog/post/share.html", {"post": post, "form": form, "sent": sent}
    )


@require_POST
def post_comment(request, id):
    post = get_object_or_404(models.Post, id=id, status=models.Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(
        request,
        "blog/post/comment.html",
        {"post": post, "form": form, "comment": comment},
    )
