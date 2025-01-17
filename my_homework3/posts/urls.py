from django.urls import path
from . import views

app_name="posts"
urlpatterns = [
    path("",views.post_list,name="list"),
    path("<int:pk>/",views.post_detail,name="detail"),
    path("new/",views.post_create,name="create"),
    path("<int:pk>/update/",views.post_update,name="update"),
    path("<int:pk>/confirm/",views.confirm_delete,name="confirm_delete"),
    path("<int:pk>/delete/",views.post_delete,name="delete"),
    path("<int:pk>/comment/",views.comment,name="comment"),
    path("<int:pk>/comment/<comment_pk>/update",views.comment_update,name="comment_update"),
    path("<int:pk>/comment/<int:comment_pk>/delelte",views.comment_delete,name="comment_delete"),
]
