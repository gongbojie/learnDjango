from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	# 构建一个字典，作为上下文传递给模板引擎
	# boldmessage键对应于模板的{{ boldmessage }}
	context_dict = { 'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!" }
	return render(request, 'rango/index.html', context=context_dict)

def about(request):
	context_dict = { 'boldmessage': "1, 2, 2, 3, 4!" }
	return render(request, 'rango/index.html', context=context_dict)