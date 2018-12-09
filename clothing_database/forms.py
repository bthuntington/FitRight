from django import forms
from .models import Color, Material, Pattern, LowerBody
from .models import UpperBody, ProductItem, ClothingPreferance, Profile


# class PreferencesForm(forms.Form):
# 	# fit = forms.ModelChoiceField(queryset=ClothingPreferance.fit)
# 	colorlist = forms.ModelChoiceField(queryset=Color.objects.all()) 
# 	material = forms.ModelChoiceField(queryset=Material.objects.all())
# 	pattern = forms.ModelChoiceField(queryset=Pattern.objects.all())

# 	# class Meta:
# 	# 	model = ProductItem
# 	# 	fields=['color']