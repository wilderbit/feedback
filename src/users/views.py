from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
# Create your views here.


def home(req):
    return render(request=req, template_name="index.html")


def login_user(req):
    logout(req)
    if req.POST:
        email = req.POST["email"]
        password = req.POST["password"]
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(req, user)
                pass
