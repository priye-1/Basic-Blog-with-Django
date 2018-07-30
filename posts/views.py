from django.shortcuts import render, render_to_response, get_object_or_404
from django import template
from django.http import HttpResponse
from .models import Post
from django.views import generic
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    """Display Home page"""
    return render(request, "posts/index.html", {})


def postList(request):
    """Post list view"""
    # reversing objects and turning into a list to access the length
    posts = Post.objects.all().filter(
        is_draft=False).order_by('-date_created')[0:10]
    context = {"posts": posts}
    return render(request, "posts/post_list.html", context)


def create(request):
    """Post create from view"""
    if request.method == "POST":
        form = PostForm(data=request.POSt)
        return redirect(to=post.get_absolute_url())

    # Render form if Get reguest
    return render(request, "posts/create.html", {})


def detail(request, post_id):
    """Post detail view"""
    post = get_object_or_404(Post, id=post_id)
    context = {"post": post}
    return render(request, "posts/detail.html", context)


def edit(request, post_id):
    """Post edit view"""
    message = "You are editing post of post id: %s" % str(post_id)
    return HttpResponse(message)


def update(request, post_id):
    """Post Update view"""
    message = "You are updating post of post id: %s" % str(post_id)
    return HttpResponse(message)


def delete(request, post_id):
    """Post Update view"""
    message = "You are deleting post of post id: %s" % str(post_id)
    return HttpResponse(message)


def byAuthor(request):
    """Display page by author"""
    posts = list(reversed(Post.objects.all()))
    names = Post.objects.all().filter(publisher__username="priye")
    context = {"posts": posts, "names": names}

    return render(request, "posts/byAuthor.html", context)


def search(request):
    """To carry out search functions"""
    template = "posts/results.html"
    query = request.GET.get('q')
    results = Post.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query) |
        Q(publisher__username__icontains=query)
    )
    return render(request, template, {"results": results})


def all_authors(request):
    """View all authors"""
    template = "posts/all_authors.html"
    posts = Post.objects.all()
    context = {"posts": posts}
    # final_list= []
    # for name in posts:
    #     if name not in final_list:
    #         final_list.append(name)

    # 'email', flat=True).distinct()

    return render(request, template, context)
