from django.shortcuts import render
from django.http import HttpResponse
from checkins.forms import MoodEntryForm
from .models import MoodEntry



def home(requests):
    # return HttpResponse("Welcome to my website")
    return render(requests, "checkins/home.html")

def get_form(requests):
    
    if requests.method == 'POST':
        my_form = MoodEntryForm(requests.POST)
        
        if my_form.is_valid():
            saved_mood = my_form.save()
            return render(requests, 'checkins/success.html', {'mood' : saved_mood})
        
    else:
        my_form = MoodEntryForm()
        
    return render(
        requests,
        "checkins/entry_form.html",
        {"django_form": my_form}
    )
