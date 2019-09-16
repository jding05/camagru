from django.db import models

from webcam.models import Post
# Create your models here.
class Comment(models.Model):
	img_id = models.IntegerField()
	login = models.CharField(max_length=255, null=False)
	comment = models.CharField(max_length=255, null=False)
	postdate = models.DateTimeField(auto_now_add=True, null=False)
	post = models.ForeignKey(Post,on_delete=models.CASCADE)


class Like(models.Model):
	img_id = models.IntegerField()
	login = models.CharField(max_length=255, null=False)
	post = models.ForeignKey(Post,on_delete=models.CASCADE)