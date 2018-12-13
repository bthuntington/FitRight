from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Color, Material, Pattern, lower_body
from .models import upper_body, product_item, ClothingPreferance, Profile
from django.db import connection

# Create your views here.

def home(request):
    profile = Profile.objects.all()
    return render(request, 'clothing_database/home.html', {'profile': profile})

def view_database(request):
    	if request.method == 'POST':
    		if(request.POST.get('profile_id')):
    			profile_id = request.POST['profile_id']
    			user = Profile.objects.get(profile_id=profile_id)
    			profile_name = user.profile_name
    			request.session['profile_name'] = profile_name
    			request.session['profile_id'] = profile_id
    			prefs = ClothingPreferance.objects.get(profile_id=profile_id)
    			request.session['material'] = prefs.material
    			request.session['pattern'] = prefs.pattern
    			request.session['color'] = prefs.color
    			request.session['price_min'] = prefs.price_min
    			request.session['price_max'] = prefs.price_max
    			request.session['lightness'] = prefs.lightness
    			return render(request, 'clothing_database/view_database.html', {'profile_name': profile_name, 'profile_id': profile_id})

    	return render(request, 'clothing_database/home.html',)

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
			# user.profile_id = user.pk
			user.save()
			user = Profile.objects.get(profile_name=profile_name)
			users = Profile.objects.all()
			# prof_name = Profile.objects.get(id=use)

			if(request.POST.get('fit') and request.POST.get('color') 
				and request.POST.get('pattern') and request.POST.get('material')
				and request.POST.get('price_min') and request.POST.get('price_max')):
				fit = request.POST['fit']
				color = request.POST['color']
				fit = request.POST['fit']
				color = request.POST['color']
				pattern = request.POST['pattern']
				material = request.POST['material']
				price_min = request.POST['price_min']
				price_max = request.POST['price_max']
				# prefs = ClothingPreferance(profile_id= profile_id,
				# 	profile_name=Profile.objects.get(profile_id=profile_id, profile_name=name, password=password), material=material, pattern=pattern,
				# 	fit=fit, color=color, lightness=5, price_min=price_min, price_max=price_max)
				# prefs.save()
				# waist = request.POST['waist']
				# hips = request.POST['hips']
				# thigh = request.POST['thigh']
				# knee = request.POST['knee']
				# calf = request.POST['calf']
				# instep = request.POST['instep']
				# side_to_knee = request.POST['side_to_knee']
				# side_length = request.POST['side_length']
				# crotch_depth = request.POST['crotch_depth']
				# crotch_length = request.POST['crotch_length']
				# lower_body = lower_body(ub_id=user.profile_id, ub_name= user.profile_name, waist= waist, hips= hips, thigh=thigh, knee=knee, calf=calf, instep = instep, 
				# 		side_to_knee=side_to_knee, side_length=side_length, crotch_depth=crotch_depth, crotch_length=crotch_length)
				# lower_body.save()

				return render(request, 'clothing_database/view_database.html')
	return render(request, 'clothing_database/create_account.html')


class DatabaseListView(generic.ListView):
	model = product_item
	context_object_name = 'product_list'
	object_list = product_item.objects.all()
	template_name = 'clothing_database/view_database.html'

	def post(self, request):
		user_pattern = request.session['pattern']
		user_material = request.session['material']
		user_color = request.session['color']
		user_price_min = request.session['price_min']
		user_price_max = request.session['price_max'] 
		user_lightness = request.session['lightness']
		profile_id = request.session['profile_id']
		profile_name = request.session['profile_name']
		# Lb, ub queries
		list = []
		product_list = product_item.objects.all()
		if "lb_values" in request.POST:
			cursor = connection.cursor()
			cursor.execute("SELECT * FROM product_item WHERE brand_name = ANY (SELECT DISTINCT lb1.lb_name AS brand_name FROM lower_body lb1 JOIN lower_body lb2 JOIN profile WHERE lb1.thigh <= (lb2.thigh + 2) AND lb1.thigh = (lb2.thigh) AND lb2.waist <= (lb2.waist + 2) AND lb1.instep <= (lb2.instep + 2)) GROUP BY brand_id")
			for obj in cursor.fetchall():
				dict = {"item_id": obj[0], "brand_id": obj[1], "brand_name": obj[2], "product_name": obj[3],"material": obj[4], "pattern": obj[5], "color": obj[6], "lightness": obj[7], "price": obj[8]}
				list.append(dict) 
			product_list = list
		elif "ub_values" in request.POST:
			cursor = connection.cursor()
			cursor.execute("SELECT * FROM product_item WHERE brand_id = ANY (SELECT DISTINCT ub1.ub_id AS brand_id FROM upper_body ub1 JOIN upper_body ub2 JOIN profile WHERE profile_id = ub1.ub_id AND ub1.chest <= (ub2.chest + 2) AND ub1.chest = (ub2.chest) AND ub1.neck_to_wrist <= (ub2.neck_to_wrist + 2) AND ub1.back_to_waist <= (ub2.back_to_waist + 2)) GROUP BY brand_id")

			for obj in cursor.fetchall():
				dict = {"item_id": obj[0], "brand_id": obj[1], "brand_name": obj[2], "product_name": obj[3],"material": obj[4], "pattern": obj[5], "color": obj[6], "lightness": obj[7], "price": obj[8]}
				list.append(dict) 
			product_list = list
		# Color queries
		elif "color" in request.POST and "pattern" in request.POST:
			product_list = product_item.objects.filter(color=user_color, pattern=user_pattern)
		elif "color" in request.POST and "material" in request.POST:
			product_list = product_item.objects.filter(color=user_color, material=user_material)
		elif "color" in request.POST and "brand_name" in request.POST:
			product_list = product_item.objects.filter(color=user_color, brand_name="Nike")
		elif "color" in request.POST and "lightness" in request.POST:
			product_list = product_item.objects.filter(color=user_color, lightness=user_lightness)
		elif "color" in request.POST and "price" in request.POST:
			product_list = product_item.objects.filter(color=user_color, price__range=(user_price_min,user_price_max))
		# Material Queries
		elif "material" in request.POST and "pattern" in request.POST:	
			product_list = product_item.objects.filter(material=user_material, pattern=user_pattern)
		elif "material" in request.POST and "brand_name" in request.POST:	
			product_list = product_item.objects.filter(material=user_material, brand_name="Nike")
		elif "material" in request.POST and "lightness" in request.POST:	
			product_list = product_item.objects.filter(material=user_material, lightness=user_lightness)
		elif "material" in request.POST and "price" in request.POST:	
			product_list = product_item.objects.filter(material=user_material, price__range=(user_price_min,user_price_max))
		elif "pattern" in request.POST and "brand_name" in request.POST:
			product_list = product_item.objects.filter(pattern=user_pattern, brand_name="Nike")
		elif "pattern" in request.POST and "lightness" in request.POST:
			product_list = product_item.objects.filter(pattern=user_pattern, lightness=user_lightness)
		elif "pattern" in request.POST and "price" in request.POST:
			product_list = product_item.objects.filter(pattern=user_pattern, price__range=(user_price_min,user_price_max))
		# Brand Queries
		elif "brand" in request.POST and "lightness" in request.POST:
			product_list = product_item.objects.filter(brand_name="Nike", lightness=user_lightness)
		elif "brand" in request.POST and "price" in request.POST:
			product_list = product_item.objects.filter(brand_name="Nike", price__range=(user_price_min,user_price_max))
		elif "lightness" in request.POST and "price" in request.POST:
			product_list = product_item.objects.filter(lightness=user_lightness, price__range=(user_price_min,user_price_max))
		elif "color" in request.POST: 
			product_list = product_item.objects.filter(color=user_color)
		elif "pattern" in request.POST:
			product_list = product_item.objects.filter(pattern=user_pattern)
		elif "material" in request.POST:
			product_list = product_item.objects.filter(material=user_material)
		elif "brand" in request.POST:
			product_list = product_item.objects.filter(brand_name="Nike")
		elif "lightness" in request.POST:
			product_list = product_item.objects.filter(lightness=user_lightness)
		elif "price" in request.POST:
			product_list = product_item.objects.filter(price__range=(user_price_min, user_price_max))
		else:
			product_list = product_item.objects.all()
		
		length = len(product_list)
		return render(request, 'clothing_database/view_database.html', {'product_list': product_list, 'profile_id': profile_id, 'profile_name': profile_name, 'list': list, 'length': length})
		
