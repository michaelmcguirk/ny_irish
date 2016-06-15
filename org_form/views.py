from django.shortcuts import render

def index(request):
	template = 'org_form/index.html'
	return render(request, 'org_form/index.html')

# Create your views here.
