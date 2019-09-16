from django.contrib import admin

from post.models import Comment
from post.models import Like
# Register your models here.
admin.site.register(Comment)
admin.site.register(Like)