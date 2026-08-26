from django.shortcuts import render
from django.http import HttpResponse
from checkins.forms import MoodEntryForm
from .models import MoodEntry
from django.db.models import Avg



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
    
def report(requests):
    # Query parametrs is like when the urls get ? and showing the date in url. e.g : report/?date=2026-08-26
    # If we want to filter the whole form, we should use GET method. because you're jusr submitting and the result should be shown is URL : GET method. 
    entry = MoodEntry.objects.all()
    selected_date = requests.GET.get('date')
    low_only = requests.GET.get('low')
    low_energy = requests.GET.get('low_energy')
    
    if selected_date :
        entry = entry.filter(created_at__date = selected_date)
        
    # If we checked the checkbox : /?date=2026-08-25&low=1, else : like before with a date e.g if you give a date.
    
    if low_only :
        entry = entry.filter(score__lte=2)
        
    if low_energy :
        entry = entry.filter(energy_level__lte = 2)
        
    avg_result = entry.aggregate(Avg('score'))
    avg_score = avg_result['score__avg']
        
    return render(
        requests,
        "checkins/success.html",
        # selected_date, low_only, avg_score
        {"entries": entry, "count": entry.count(),
         'avg_score' : avg_score,
         'date' : selected_date,
         'low_only' : low_only,
         'low_energy' : low_energy
         }
    )