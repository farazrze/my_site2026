from django.shortcuts import render
from django.http import HttpResponse
from mainpages.forms import Contact_form

def index(request):
    return render(request,"website/index.html")
def about(request):
    return render(request,"website/about.html")

def contact(request):
    if request.method == "POST":
        form = Contact_formm(request.POST)
        if form.is_valid:
            form.save()
    form=Contact_formm()
    return render(request,"website/contact.html",form)
