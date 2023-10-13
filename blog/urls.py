from django.urls import path, include
from . import views


app_name = "blog"

urlpatterns = [
    path("", views.posts_list, name="posts_list"),
    path("tag/<slug:tag_slug>/", views.posts_list, name="posts_list_by_tag"),
    # path("", views.PostListView.as_view(), name="posts_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_details,
        name="post_details",
    ),
    path("<int:id>/share/", views.post_share, name="post_share"),
    path("<int:id>/comment/", views.post_comment, name="post_comment"),
]
