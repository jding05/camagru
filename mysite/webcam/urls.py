from django.urls import path
from django.views.generic.base import TemplateView


from . import views

app_name = 'webcam'
urlpatterns = [
	path("", views.webcam, name="webcam"),
]

