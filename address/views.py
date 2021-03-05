from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from django.db.models import Q 

'''
def home(request):
	all_contacts = Contact.objects.all
	return render(request, 'home.html', {'all_contacts': all_contacts})
'''

def add(request):
	if request.method == "POST":
		form = ContactForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ('Contact has been added!'))
			return redirect('home')		
		else:
			messages.success(request, ('Error.  Please try again.'))	
			return render(request, 'add.html', {})	
	else:
		return render(request, 'add.html', {})	

def edit(request, list_id):
	if request.method == "POST":
		get_contact = Contact.objects.get(pk=list_id)
		form = ContactForm(request.POST or None, instance=get_contact)
		if form.is_valid():
			form.save()
			messages.success(request, ('Contact Has Been Edited!'))
			return redirect('home')
		else:
			messages.success(request, ('Seems Like There Was An Error...'))	
			return render(request, 'edit.html', {})	
	else:
		get_contact = Contact.objects.get(pk=list_id)
		return render(request, 'edit.html', {'get_contact': get_contact})	

def delete(request, list_id):
	if request.method == "POST":
		current_contact = Contact.objects.get(pk=list_id)
		current_contact.delete()
		messages.success(request, ('Contact Has Been Deleted!'))
		return redirect('home')
	else:
		messages.success(request, ('Nothing To See Here...'))	
		return redirect('home')	

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Contact
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Contact.objects.filter(
            Q(name__icontains=query) | Q(address=query) | Q(city=query) | Q(state__icontains=query) | Q(zipcode__icontains=query)
        )
        return object_list