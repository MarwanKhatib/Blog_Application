from django.urls import path, include
from . import views


app_name = "blog"

urlpatterns = [
    path("", views.posts_list, name="posts_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/", views.post_details, name="post_details"),
]
