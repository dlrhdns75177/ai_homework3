from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile
from django.shortcuts import get_object_or_404

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


def new_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("users:profile")
    else:
        form = ProfileForm()
    context = {
        "form":form
    }
    return render(request,"users/new_profile.html",context)

@login_required
def user_profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    '''
    Profile 테이블의 user 필드는 onetoone필드니까 해당 모델이랑 연결해줘야한다(user=request.user)
    프로필 페이지에서 보여주기만 하면 되니까 post없이 get 요청만
    '''
    if not profile:
        return redirect("users:new_profile")
    context = {
        "profile":profile
    }
    return render(request,"users/profile.html",context)


def edit_profile(request):
    pass

