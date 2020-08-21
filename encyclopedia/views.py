from django.shortcuts import render,redirect,reverse
from django import forms
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from . import util
from markdown2 import Markdown
import random 

# create form class for queries
class QueryForm(forms.Form):
	query=forms.CharField(label='Search')

# create form class for new pages
class NewPageForm(forms.Form):
	page=forms.CharField(label='Page Title')

# instantiate markdown

markdown = Markdown()

def index(request):
    
    # determine whether method = post
    if request.method=='POST':

    	# take in query entered by user
        form=QueryForm(request.POST)
        # check whether form is valid
        if form.is_valid():
        	# assign query to variable
            query=form.cleaned_data["query"]

            # if query in list of entries, return query results page
            if util.get_entry(query):
            	return redirect('encyclopedia:return_results', query)

            # if query is in list of substrings render index page with related results
            elif util.get_substrings(query) != None:
            	return render(request, "encyclopedia/index.html", {
    				"entries": util.get_substrings(query),
    				"form":QueryForm()
    				})
            # return error page if query not in list of entries or substrings
            else:
            	return render(request, "encyclopedia/error.html", {
    				"entries": util.list_entries()
    				})
                

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form":QueryForm()
    })

# render markdown file for list items
def return_results(request,title):
	title = title.lower()
	entry = util.get_entry(title)

	if entry is None:
		return render(request, "encyclopedia/error.html", {
            "form":QueryForm()
            })
	
	else:
		return render(request, "encyclopedia/results.html", {
			"entry": markdown.convert(entry), 
			"title":title,
			"form":QueryForm()
			})	

# render random page from list of entries
def random_page(request):
	# entry = random.choice(util.list_entries())
	return redirect("encyclopedia/results.html", {
		"entry":random.choice(util.list_entries())
		})

def add_entry():
    return render("encyclopedia/create_page.html")



def save_entry(request):

    # determine whether method = post
    if request.method=='POST':

    	# take in query entered by user
        form=NewPageForm(request.POST)
        # check whether form is valid
        if form.is_valid():
        	# assign query to variable
            page=form.cleaned_data["page"]

            # if page already exists, render error page
            if util.get_entry(page):
            	return render('encyclopedia/error.html')

            # TODO: if page doesn't exist, save and create new
            else:
            	return render(request, "encyclopedia/error.html", {
    				"title": page,
    				# "content": 
    				})
                

    return render(request, "encyclopedia/create_page.html", {
        "entries": util.list_entries(),
        "form":QueryForm()
    })
