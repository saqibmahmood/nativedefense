from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Eat no fruit for the entire month",
    "march": "Eat no basil for the entire month",
    "april": "Eat no chicken for the entire month",
    "may": "Eat no veggies for the entire month",
    "june": "Eat no lentils for the entire month",
    "july": "Eat no fish for the entire month",
    "august": "Drink no soda for the entire month",
    "september": "Drink no juice for the entire month",
    "october": "Drink no alcohol for the entire month",
    "november": "Drink no energy drinks for the entire month",
    "december": "No sleep for the entire month ;)"
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args = [month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'
    resopnse_data = f"<ul>{list_items}</ul>"
    return HttpResponse(resopnse_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1> {challenge_text} </h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")