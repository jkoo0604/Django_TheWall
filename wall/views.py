from django.shortcuts import render, redirect
from .models import *
from login.models import User
from datetime import datetime, timedelta
import pytz

# Create your views here.
def index(request):
    #Display all messages
    #   Newest post on top
    #   Oldest comment on top
    # print(Message.objects.all())
    if 'userid' in request.session:
        context = {
            'current_user': User.objects.get(id=request.session['userid']),
            'all_messages': Message.objects.all().order_by('-created_at'),
        }
        return render(request,'wall.html',context)
    return redirect('/')

def createPost(request):
    #Process POST request for new post
    #   Redirect to index
    if request.method == 'POST':
        if len(request.POST['newpost']) > 0:
            Message.objects.create(message=request.POST['newpost'],user_id_id=request.session['userid'])
        context = {
            'current_user': User.objects.get(id=request.session['userid']),
            'all_messages': Message.objects.all().order_by('-created_at'),
        }
        if request.is_ajax():
            return render(request,'posts-index.html',context)
        # else:
        #     return render(request,'wall.html',context)
    return redirect('/')

def createComment(request):
    #Process POST request for new comment
    #   Redirect to index
    if request.method == 'POST':
        if len(request.POST['newcomment']) > 0:
            Comment.objects.create(message_id_id=int(request.POST['message_id']),user_id_id=request.session['userid'],comment=request.POST['newcomment'])
        context = {
            'current_user': User.objects.get(id=request.session['userid']),
            'all_messages': Message.objects.all().order_by('-created_at'),
        }   
        if request.is_ajax():
            return render(request,'posts-index.html',context)
        # else:
        #     return render(request,'wall.html',context)
    return redirect('/')

def deleteComment(request, commentid):
    #Process POST?? request to delete comment made by user who posted it
    #   Check created_at < 30 min from current utc time
    #   If true, delete comment
    #   Redirect to index

    comment = Comment.objects.get(id=commentid)
    if comment.user_id.id == request.session['userid']:
        comment_time = comment.created_at
        current_time = datetime.now(pytz.utc)
        print(comment_time)
        print(current_time)
        if comment_time > current_time - timedelta(minutes = 30):
            comment.delete()
        context = {
            'current_user': User.objects.get(id=request.session['userid']),
            'all_messages': Message.objects.all().order_by('-created_at'),
        }
        if request.is_ajax():   
            return render(request,'posts-index.html',context)
        # else:
        #     return render(request,'wall.html',context)
    return redirect('/')

def deletePost(request, postid):
    #Process POST?? request to delete message made by user who posted it
    #   Check created_at < 30 min from current utc time
    #   If true, delete message
    #   All associated comments will be deleted (on_delete = cascade)
    #   Redirect to index
    post = Message.objects.get(id=postid)
    if post.user_id.id == request.session['userid']:
        post_time = post.created_at
        current_time = datetime.now(pytz.utc)
        print(post_time)
        print(current_time)
        if post_time > current_time - timedelta(minutes = 30):
            post.delete()
        context = {
            'current_user': User.objects.get(id=request.session['userid']),
            'all_messages': Message.objects.all().order_by('-created_at'),
        }   
        if request.is_ajax():
            return render(request,'posts-index.html',context)
        # else:
        #     return render(request,'wall.html',context)
    return redirect('/')
