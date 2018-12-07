from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic

from clothing_database.models import Profile

# Create your views here.

def home(request):
    profile = Profile.objects.all()
    # User.objects.all()
    return render(request, 'clothing_database/home.html', {'profile': profile})

def detail_site(request):
	return HttpResponse("Hola, this is where the database will be shown with options")
def create_account(request):
	 return render(request, 'clothing_database/create_account.html')


class DatabaseListView(generic.ListView):
    model = Profile
    context_object_name = Profile
    template_name = 'clothing_database/home.html'