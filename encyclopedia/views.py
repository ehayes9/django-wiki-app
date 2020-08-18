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

            if not util.get_entry(query):
            	return render(request, "encyclopedia/error.html", {
    				"entries": util.list_entries()
    				})

            else:
                return redirect('encyclopedia:return_results', query)

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form":QueryForm(),
        "head":"All Pages"
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





