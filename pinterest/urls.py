from django.urls import re_path,path
from . import views
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Pin

def index(request):
	context = {'pins_list': Pin.objects.all()}
	return render(request, 'pinterest/index.html', context)

urlpatterns = [
	# ex: /pinterest/
	re_path(r'^$', index, name='index')
]