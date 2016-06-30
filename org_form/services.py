from .models import Organisation
from django.db.models import Q

def org_search(search_query):
	results = Organisation.objects.filter(Q(name__icontains=search_query) 
		| Q(address_1__icontains=search_query) | Q(state__icontains=search_query))
	return results