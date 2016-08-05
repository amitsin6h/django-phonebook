from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import PhoneBookForm
from . models import PhoneBook 
# Create your views here.



def add_contact(request):
	form = PhoneBookForm()
	contact = PhoneBook.objects.all()
	if request.method == 'POST':
		form = PhoneBookForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return HttpResponseRedirect('/')
		else:
			form = PhoneBookForm()		
	return render(request, 'index.html', {'form':form, 'contact':contact})
