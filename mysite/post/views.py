from django.shortcuts import render
from webcam.models import Post
from .models import Comment, Like

from datetime import datetime
# Create your views here.

def post(request, post_id):
	if request.method == 'GET':
		post = Post.objects.get(id=post_id)
		comments = Comment.objects.all()
		likes = Like.objects.all()
		return render(request, 'post.html', {'post': post, 'comments': comments, 'likes': likes})
	elif request.method == 'POST':
		login = request.user.username
		if 'comment_form' in request.POST:
			comment = request.POST.get('comment')
			add_comment(login, post_id, comment)
			likes = Like.objects.all()
			comments = Comment.objects.all()
			post = Post.objects.get(id=post_id)
			return render(request, 'post.html', {'post': post, 'comments': comments, 'likes': likes})
		elif 'like_form' in request.POST:
			post = Post.objects.get(id=post_id)
			obj, created = Like.objects.get_or_create(img_id=post_id, login=login, post=post)
			if created == False:
				obj.delete()
				print("delete like")
			likes = Like.objects.all()
			comments = Comment.objects.all()
			return render(request, 'post.html', {'post': post, 'comments': comments, 'likes': likes})


def get_now():
	return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def add_comment(login, post_id, comment):
	post = Post.objects.get(id=post_id)
	comment = Comment.objects.update_or_create(img_id=post_id, login=login, comment=comment, post=post)[0]
	print(comment.id)
	print(comment.img_id)
	print(comment.comment)
	print(comment.postdate)
	print(comment.post.id)
	return comment
