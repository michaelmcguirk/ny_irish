from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .services import org_search
from .models import Organisation

def index(request):
	template = 'org_form/index.html'
	return render(request, 'org_form/index.html')

def search(request):
	print('-------Search function------')
	template = 'org_form/search.html'
	org_list = Organisation.objects.all().order_by('name')
	paginator = Paginator(org_list, 5)
	page = request.GET.get('page')
	try:
		orgs = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		orgs = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		orgs = paginator.page(paginator.num_pages)

	context = {'orgs' : orgs}
	return render(request, template, context)

def results(request):
	print('-------Results function------')
	query = request.GET['q']
	template = 'org_form/results.html'
	result_set = org_search(query)
	paginator = Paginator(result_set, 5)
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
