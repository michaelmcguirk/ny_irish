from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
	paginator = Paginator(result_set, 10)

	page = request.GET.get('page')
	try:
		results = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		results = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		results = paginator.page(paginator.num_pages)

	context = {'query' : query, 'results' : results}
	return render(request, template, context)



# Create your views here.
