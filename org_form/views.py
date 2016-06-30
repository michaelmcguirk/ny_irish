from django.shortcuts import render
from .services import org_search

def index(request):
	template = 'org_form/index.html'
	return render(request, 'org_form/index.html')

def search(request):
	template = 'org_form/search.html'
	return render(request, template)

def results(request):
	query = request.GET['q']
	template = 'org_form/results.html'
	result_set = org_search(query)
	context = {'query' : query, 'rs' : result_set}
	return render(request, template, context)



# Create your views here.
