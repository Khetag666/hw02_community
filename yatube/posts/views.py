from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from django.conf import settings


def index(request):
    template = 'posts/index.html/'
    posts = Post.objects.select_related('group',
                                        'author')[:settings.KOL_POST]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:settings.KOL_POST]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
