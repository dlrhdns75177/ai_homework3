from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from .forms import CustomUserCreationForm

def login(request):
    if request.method =="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            next = request.GET.get("next") or "main"
            return redirect(next)
    else:
        form = AuthenticationForm()
    context = {
        "form":form
    }
    return render(request,"users/login.html",context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("main") 


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect("main")
    else:
        form = CustomUserCreationForm()
    context = {
        "form":form
    }
    return render(request,"users/signup.html",context)