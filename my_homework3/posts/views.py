from django.shortcuts import render,redirect
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.views.decorators.http import require_POST

def main(request):
    return render(request,"posts/main.html")

def post_list(request):
    post = Post.objects.all().order_by("-pk")
    context = {
        "posts":post
    }
    return render(request,"posts/post_list.html",context)

def post_detail(reqeust,pk):
    post = get_object_or_404(Post,pk=pk)
    context = {
        "post":post
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

def confirm_delete(request,pk):
    post = get_object_or_404(Post,pk=pk)
    context = {
        "post":post
    }
    return render(request,"posts/post_confirm_delete.html",context)
    
def post_delete(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect("posts:list")




