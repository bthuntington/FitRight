from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from .forms import PreferencesForm
from .models import Color, Material, Pattern, LowerBody
from .models import UpperBody, ProductItem, ClothingPreferance, Profile

# Create your views here.

def home(request):
    profile = Profile.objects.all()
    # User.objects.all()
    return render(request, 'clothing_database/home.html', {'profile': profile})

def view_database(request):
    	if request.method == 'POST':
    		if(request.POST.get('profile_id')):
    			p = request.POST['profile_id']
    			user = Profile.objects.get(profile_id=p)
    			request.session['profile_id'] = p
    			return render(request, 'clothing_database/view_database.html', {'user': user})
    	return render(request, 'clothing_database/home.html')

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
				# lowerBody = LowerBody(ub_id=user.profile_id, ub_name= user.profile_name, waist= waist, hips= hips, thigh=thigh, knee=knee, calf=calf, instep = instep, 
				# 		side_to_knee=side_to_knee, side_length=side_length, crotch_depth=crotch_depth, crotch_length=crotch_length)
				# lowerBody.save()

				return render(request, 'clothing_database/view_database.html')
	return render(request, 'clothing_database/create_account.html')


class DatabaseListView(generic.ListView):
	model = ProductItem
	context_object_name = 'product_list'
	object_list = ProductItem.objects.all()
	template_name = 'clothing_database/view_database.html'

	# def get_queryset(request, self):
	# 	queryset = ClothingPreferance.objects.all()
	# 	if request.method == "POST":
	# 		return queryset
	def get_context_data(self, **kwargs):
		context = super(DatabaseListView, self).get_context_data(**kwargs)
		context['form'] = PreferencesForm()
		return context

	def post(self, request):
		# form = PreferencesForm(request.POST)
		# if form.is_valid():
		# product_list = self.get_context_data()
		product_list = ProductItem.objects.all()
		if "color" and "pattern" in request.POST:
			product_list = ProductItem.objects.filter(color="black", pattern="stripes")
		elif "color" in request.POST: 
			product_list = ProductItem.objects.filter(color="black")
		elif "pattern" in request.POST:
			product_list = ProductItem.objects.filter(pattern="dots")
		elif "material" in request.POST:
			product_list = ProductItem.objects.filter(material="leather")
		elif "brand_name" in request.POST:
			product_list = ProductItem.objects.filter(brand_name="Gucci")
		elif "lightness" in request.POST:
			product_list = ProductItem.objects.filter(lightness=5)
		else:
			product_list = ProductItem.objects.all()
			
		return render(request, 'clothing_database/view_database.html', {'product_list': product_list})

	def get(self, request):
		form = PreferencesForm()
		return render(request, self.template_name, {'form': form})

    	# if self.request.POST.get('color'):
     #    	queryset = queryset.filter(color='blue')
    	# return queryset

    # def change_database(request):
    # 	if request.method == 'POST':
    # 		if(request.POST.get('color')):
    # 			user_id = request.session.get('profile_id')
    # 			user = Profile.objects.get(profile_id=user_id)
    # 			list = ClothingPreferance.objects.filter(val=search)
    # 			return MetaObjectList.as_view()(self.request,list)
    # 			color = ClothingPreferance.objects.filter(profile_id=user_id).values('color')
    # 			product_list = ProductItem.objects.filter(color=color)
    # 			return render(request, 'clothing_database/view_database.html', {'product_list': product_list})
    # 	return render(request, 'clothing_database/home.html')
