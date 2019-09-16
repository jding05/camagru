from django.urls import path


from . import views

app_name = 'post'
urlpatterns = [
	path('<int:post_id>/', views.post, name='post'),
]
