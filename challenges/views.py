from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def january(request):
    return HttpResponse("January")

def february(request):
    return HttpResponse("February")

def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "January"
    elif month == 'february':
        challenge_text = "February"
    else:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)