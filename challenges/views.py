from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Read 2 research articles per day.",
    "february": "Complete 30 minutes of cardio everyday",
    "march": "Refrain from eating sweets at least 5 days out of every week",
    "april": "Complete 50 burpees every other day",
    "may": "Complete 30 minutes minimum of classwork studying per day. ",
    "june": "Do 50 push-ups every morning",
    "july": "Clean your car every weekend",
    "august": "Write in journal twice per week",
    "september": "Complete 45 minutes of cardio every other day",
    "october": "Call your relative once per week",
    "november": "Do yoga every weekend",
    "december": "Wakeup by 8am everyday"
}


# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
