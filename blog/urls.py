from django.urls import path, include
from . import views


app_name = "blog"

urlpatterns = [
    # path("", views.posts_list, name="posts_list"),
    path("", views.PostListView.as_view(), name="posts_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_details,
        name="post_details",
    ),
    path("<int:id>/share/", views.post_share, name="post_share"),
]
