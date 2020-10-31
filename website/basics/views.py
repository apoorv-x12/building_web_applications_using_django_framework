from django.shortcuts import render
from django.http import HttpResponse
from .forms import InterestForm
import datetime


def welcome(request):
    return HttpResponse("<h1>Welcome To Django</h1>")


def wish(request):
    name = request.GET['name']
    return HttpResponse(f"<h1>Hello, {name}</h1>")


def topics(request):
    now = str(datetime.datetime.now())
    return render(request, 'topics.html', {'now': now})


def interest(request):
    if 'amount' in request.GET:
        amount = float(request.GET['amount'])
        rate = float(request.GET['rate'])
        interest = amount * rate / 100
        return render(request, 'interest.html', {'interest': interest})
    else:
        return render(request, 'interest.html')


def interest_post(request):
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        rate = float(request.POST['rate'])
        interest = amount * rate / 100
        return render(request, 'interest_post.html', {'interest': interest})
    else:
        return render(request, 'interest_post.html')


def interest_form(request):
    if request.method == "POST":
        form = InterestForm(request.POST)  # bind POST data to form
        if form.is_valid():
            amount = float(form.cleaned_data['amount'])
            rate = float(form.cleaned_data['rate'])
            interest = amount * rate / 100
            return render(request, 'interest_form.html',
                      {'form': form, 'interest': interest})
        else:
            return render(request, 'interest_form.html',{'form': form})
    else:  # GET request
        form = InterestForm()
        return render(request, 'interest_form.html', {'form': form})


def interest_form_custom(request):
    if request.method == "POST":
        form = InterestForm(request.POST)  # bind POST data to form
        if form.is_valid():
            amount = float(form.cleaned_data['amount'])
            rate = float(form.cleaned_data['rate'])
            interest = amount * rate / 100
            return render(request, 'interest_form_custom.html',
                      {'form': form, 'interest': interest})
        else:
            return render(request, 'interest_form_custom.html',{'form': form})
    else:  # GET request
        form = InterestForm()
        return render(request, 'interest_form_custom.html', {'form': form})