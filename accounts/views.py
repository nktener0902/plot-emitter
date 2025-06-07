from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            request.session["username"] = username
            return HttpResponseRedirect(reverse("expression:index"))
    return render(request, "accounts/login.html")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            request.session["username"] = request.POST["username"]
            return HttpResponseRedirect(reverse("expression:index"))
    else:
        form = UserCreationForm()
    return render(request, "accounts/login.html", {"form": form})


def logout(request):
    request.session.clear()
    return HttpResponseRedirect(reverse("accounts:login"))
