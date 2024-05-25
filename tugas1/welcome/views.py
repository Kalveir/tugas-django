from django.shortcuts import render, HttpResponse

def welcome(request, name):
	context = {
		'name' : name
	}
	return render(request, 'welcome/index.html', context)

# Create your views here.
