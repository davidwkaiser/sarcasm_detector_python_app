from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader


def index(request):
	template = loader.get_template('texts/index.html')
	context = {}
	return HttpResponse(template.render(context, request))	
    # return render(request, 'texts/index.html', context)