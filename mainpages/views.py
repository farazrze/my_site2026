from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from mainpages.forms import Contact_form,newsletter_form

def index(request):
    return render(request,"website/index.html")
def about(request):
    return render(request,"website/about.html")

def contact(request):
    if request.method == "POST":
        form = Contact_form(request.POST)
        if form.is_valid:
            form.save()
    form=Contact_form()
    return render(request,"website/contact.html",{"form":form})


def newsletter(request):
    if request.method == "POST":
        form = newsletter_form(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/')