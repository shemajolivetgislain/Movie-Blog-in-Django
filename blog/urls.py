from typing import Pattern
from django import urls
from django.contrib.postgres import search
from django.urls import path
from .views import AddPostView, DeletePostView, UpdatePostView, home, detail, searched_posts, tagdetail

app_name = 'blog'


urlpatterns = [
    # solve home conflicts, also in core app
    path('', home, name='home'),
    path('<int:id>/', detail, name='detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('update_post/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('delete_post/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('tag_detail/<str:tag>', tagdetail, name='tag_detail'),
    path('search/', searched_posts, name='search')
]
# myabout=About.objects.all()
