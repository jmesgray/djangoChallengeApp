from django.urls import path  # so we can create paths
from . import views  # importing our views.py file

# then go to this file, to complete your view and url
urlpatterns = [
    path("", views.index, name="index"),  # will trigger for /challenges/
    path("<int:month>", views.monthly_challenge_by_number),  # integer values by user will trigger this view
    path("<str:month>", views.monthly_challenge, name="month-challenge")
    # this is a placeholder and the placeholder can be a word of your choice

]  # this is a url config. No longer need to list every month because of the placeholder
