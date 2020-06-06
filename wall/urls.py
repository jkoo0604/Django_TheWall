from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index), 
    path('post', views.createPost),
    path('comment', views.createComment),
    path('deletecomment/<int:commentid>', views.deleteComment),
    path('deletepost/<int:postid>', views.deletePost),
]