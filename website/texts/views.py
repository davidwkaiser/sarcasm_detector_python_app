from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from texts import ModelHolder


def index(request):
	template = loader.get_template('texts/index.html')
	context = {}
	return HttpResponse(template.render(context, request))	


def show(request):
	model_holder = ModelHolder.ModelHolder()
	model_holder.load_models()
	original_text = request.POST.get('inputtext')
	vectorized_text = model_holder.cvec.transform([original_text]) 
	prediction = model_holder.lr.predict(vectorized_text)
	determination = "sarcastic" if prediction[0]==1 else "not sarcastic"

	template = loader.get_template('texts/show.html')
	context = {
        'original_text': original_text, 
        'determination': determination
    }

	return HttpResponse(template.render(context, request))	
