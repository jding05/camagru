from django.db import models

# Create your models here.

# django orm auto-generate id as primary key in default
class Post(models.Model):
	login = models.CharField(max_length=255, null=False)
	image = models.CharField(max_length=255, null=False)
	postdate = models.DateTimeField(auto_now_add=True, null=False)

