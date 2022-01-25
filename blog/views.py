from django import forms
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.postgres.search import SearchVector

from .forms import CommentForm
from .models import Post

# Create your views here.


def home(request):
    posts = Post.objects.all().order_by('-date_added')
    return render(request, 'home.html', {'posts': posts})


def searched_posts(request):
    if request.method == "GET":
        search = request.GET['search']
        posts = Post.objects.filter(title__contains=search)
        return render(request, 'search.html', {'search': search, 'posts': posts})
    else:
        return render(request, 'search.html', {})


def tagdetail(request, tag):
    posts = Post.objects.filter(tags__name__in=[tag])
    return render(request, 'tag_detail.html', {'posts': posts})


def detail(request, id):
    post = Post.objects.get(id=id)
    related_posts = post.tags.similar_objects()
    tags = post.tags.names()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('blog:detail', id=post.id)
    else:
        form = CommentForm()

    return render(request, 'detail.html', {'post': post, 'form': form, 'related_posts': related_posts, 'tags': tags, })


# Class based views


class AddPostView(CreateView):
    model = Post
    # form_class = PostForm
    template_name = 'add_post.html'
    fields = ['title', 'intro', 'author', 'image', 'body', 'tags']


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'image', 'intro' 'body', 'tags']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog:home')
