from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Color, Material, Pattern, LowerBody
from .models import UpperBody, ProductItem, ClothingPreferance, Profile

# Create your views here.

def home(request):
    profile = Profile.objects.all()
    # User.objects.all()
    return render(request, 'clothing_database/home.html', {'profile': profile})

def view_database(request):

	return render(request, 'clothing_database/view_database.html')
def create_account(request):
	if request.method == 'POST':
		if (request.POST.get('name') and request.POST.get('password')
			and request.POST.get('gender') and request.POST.get('age')):
			name = request.POST['name']
			password = request.POST['password']
			age = request.POST['age']
			gender = request.POST['gender']
			profile_id = request.POST['age']
			user = Profile(profile_id=profile_id, profile_name=name, password=password, gender=gender,age=age)
			user.save()

			# if(request.POST.get('fit') and request.POST.get('color') 
			# 	and request.POST.get('pattern') and request.POST.get('material')
			# 	and request.POST.get('price_min') and request.POST.get('price_max')):
			# 	fit = request.POST['fit']
			# 	color = request.POST['color']
			# 	fit = request.POST.get['fit']
			# 	color = request.POST.get['color']
			# 	pattern = request.POST.get['pattern']
			# 	material = request.POST.get['material']
			# 	price_min = request.POST.get['price_min']
			# 	price_max = request.POST.get['price_max']
			# 	prefs = ClothingPreferance(profile_id= profile_id, 
			# 		profile_name=profile_name, material=material, pattern=pattern,
			# 		fit=fit, color=color, lightness=5, price_min=price_min, price_max=price_max)
			# 	prefs.save()
			return render(request, 'clothing_database/view_database.html')
	return render(request, 'clothing_database/create_account.html')


class DatabaseListView(generic.ListView):
    model = Profile
    context_object_name = Profile
    template_name = 'clothing_database/home.html'
