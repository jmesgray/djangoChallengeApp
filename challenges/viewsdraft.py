from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse  # this is needed to make our urls paths more dynamic and prevent bugs

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


# if you needed to add a new month you can simply add it above without touching anything else below.

# Create your views here. This is the first file you go to to create a view

def index(request):  # dont want to hardcode but instead use reverse function
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })
# above will be a long string of list by list items with tags and urls which creates the homepage


def monthly_challenge_by_number(request, month):  # whatever number user inputs will appear on the page as content
    months = list(monthly_challenges.keys())  # converting numeric inputs to months

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]  # making list start from 1 instead of 0
    redirect_path = reverse("month-challenge", args=[
        redirect_month])  # /challenge/january, reverse figures out how to create a full path for monthly-challenges
    return HttpResponseRedirect(
        redirect_path)  # using this code chunk to redirect the url for numeric inputs
    # this will be triggered if user inputs a number in url directory


# 302 is a redirect and 200 response means run was successful


def monthly_challenge(request, month):  # inputting the placeholder word of choice as an argument
    # this code chunk will be triggered if a string value is entered by user.
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text, # challenge_text is each month's action
            "month_name": month  # adding more dynamic data to our webpage for each month. First letter will be capitalized
        })  # we use this line instead of render_to_string module. Request is needed for this function

    except:
        return HttpResponseNotFound(
            "<h1>This month is not supported</h1>")  # this code is better than a long ifelse code chunk
