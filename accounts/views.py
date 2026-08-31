from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required

def acc_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(request,username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect("/")

        form = AuthenticationForm()
        context = {"form":form}
        return render(request,"accounts/login.html",context)

    else:
        return redirect("/")

 
def acc_signup(request):
    if not request.user.is_authenticated:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        return redirect("/")
    return render(request,"accounts/signup.html")


@login_required
def acc_logout(request):
    logout(request)
    return redirect("/")