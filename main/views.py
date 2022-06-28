from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from main.forms import NewUserForm


def homepage(request):

    messages.add_message(request, messages.INFO, 'Hello world.')
    return render(
        request,
        template_name="base.html",
        context={}
    )

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'User registered.')
            messages.add_message(request, messages.INFO, 'User logged in.')
            return redirect("/")

    form = NewUserForm()
    return render(
        request=request,
        template_name="main/register.html",
        context={'register_form': form}
    )