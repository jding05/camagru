from django.shortcuts import render
from webcam.models import Post
from django.contrib.auth.models import User
from django.contrib import messages
from post.models import Comment, Like

def home(request):
	if request.method == 'GET':
		posts = Post.objects.all()
		return render(request, 'home.html', {'posts': posts})
	elif request.method == 'POST':
		username = request.user.username
		post_id = int(request.POST.get('post_id'))  
		post = Post.objects.get(id=post_id)
		if username == post.login:
			post.delete()
			posts = Post.objects.all()
			return render(request, 'home.html', {'posts': posts})
		else:
			posts = Post.objects.all()
			return render(request, 'home.html', {'posts': posts})

# def post(request, post_id):
# 	post = Post.objects.get(id=post_id)
# 	return render(request, 'post.html', {'post': post})