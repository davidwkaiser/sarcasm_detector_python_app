from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader


def index(request):
	template = loader.get_template('texts/index.html')
	context = {}
	return HttpResponse(template.render(context, request))	


def show(request):
	original_text = request.POST.get('inputtext')
	template = loader.get_template('texts/show.html')
	context = {
        'original_text': original_text
    }

	return HttpResponse(template.render(context, request))	
