from django.urls import path
from . import views


app_name ="users"
urlpatterns = [
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("signup/",views.signup,name="signup"),
    path("new_profile/",views.new_profile,name="new_profile"),
    path("profile/",views.user_profile,name="profile"),
    path("profile/edit/",views.edit_profile,name="edit"),
]


