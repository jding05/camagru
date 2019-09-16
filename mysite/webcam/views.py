from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json as simplejson
from .models import Post
from django.contrib.auth.models import User

from datetime import datetime

from PIL import Image
import base64
from io import BytesIO, StringIO
import re
# Create your views here.

def webcam(request):
	if request.is_ajax():
		data = request.POST
		if data["action"] == "merge":
			image = data["content"]
			imagedata = re.sub('^data:image/.+;base64,', '', image)
			imagedata += '=' * (-len(imagedata) % 4)
			imagedata = Image.open(BytesIO(base64.b64decode(imagedata)))
			imagedata = imagedata.convert('L')
			## testing 
			# imagedata.save("test.png")
			buffered = BytesIO()
			imagedata.save(buffered, format="PNG")
			encodeimg = "data:image/png;base64," + base64.b64encode(buffered.getvalue()).decode()
			
			# test
			# testimg = re.sub('^data:image/.+;base64,', '', encodeimg)
			# testimg = Image.open(BytesIO(base64.b64decode(testimg)))
			# testimg.save("re.png")
			context = {"finish" : encodeimg}
			return JsonResponse(context, safe=False)

		else:
			username = request.user.username
			add_post(username, data["content"])
			buffered = BytesIO()
			# context = {"stored" : buffered}
			context = {}
			return JsonResponse(context, safe=False)
	else :
		print("inside webcam()")
		return render(request, 'webcam.html')

def get_now():
	return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		

def add_post(login, image): 
	post = Post.objects.update_or_create(login=login, image=image, postdate=get_now())[0]
	print(post.id)
	print(post.login)
	print(post.postdate)
	return post


