from django.shortcuts import render
from .models import place, Team


# Create your views here.
def index(request):
    # fetching
    obj1 = place.objects.all()
    obj2 = Team.objects.all()
    return render(request, "index.html", {'result': obj1, 'teams': obj2})


def home(request):
    return render(request, 'home.html')
