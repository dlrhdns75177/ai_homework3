from django.shortcuts import render,redirect
from .models import Post, Comment
from django.shortcuts import get_object_or_404
from .forms import PostForm, CommentForm
from django.views.decorators.http import require_POST,require_GET,require_http_methods
from django.contrib.auth.decorators import login_required

def main(request):
    return render(request,"posts/main.html")

@login_required
def post_list(request):
    post = Post.objects.all().order_by("-pk")
    context = {
        "posts":post
    }
    return render(request,"posts/post_list.html",context)

def post_detail(reqeust,pk):
    post = get_object_or_404(Post,pk=pk)
    comment_form = CommentForm()
    comment = post.comment.all().order_by("-pk")
    comment_count = post.comment.count()
    context = {
        "post":post,
        "comment_form":comment_form,
        "comments":comment,
        "count":comment_count
    }
    return render(reqeust,"posts/post_detail.html",context)

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("posts:detail",post.pk)
    else:
        form = PostForm()
        context = {
            "form":form
        }
    return render(request,"posts/post_form.html",context)

def post_update(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method =="POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save()
            return redirect("posts:detail",post.pk)
    else:
        form = PostForm(instance=post)
        context = {
            "post":post,
            "form":form
        }
    return render(request,"posts/post_form.html",context)

@require_GET
def confirm_delete(request,pk):
    post = get_object_or_404(Post,pk=pk)
    context = {
        "post":post
    }
    return render(request,"posts/post_confirm_delete.html",context)

@require_POST
def post_delete(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect("posts:list")

@require_POST
def comment(request,pk):
    post = get_object_or_404(Post,pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.save()
        return redirect("posts:detail",pk)

@require_http_methods(['GET','POST'])
def comment_update(request, pk, comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    if request.method == "POST":
        form = CommentForm(request.POST,instance=comment)
        if form.is_valid():
            form.save()
            return redirect("posts:detail",pk)
    else:
        form = CommentForm(instance=comment)
    context = {
        "pk":pk,
        "comment_pk":comment_pk,
        "form":form
    }
    return render(request,"posts/comment_update.html",context)


@require_POST
def comment_delete(request,pk,comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    comment.delete()
    return redirect("posts:detail",pk)



