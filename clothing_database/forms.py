from django import forms
from .models import Color, Material, Pattern, LowerBody
from .models import UpperBody, ProductItem, ClothingPreferance, Profile


class PreferencesForm(forms.Form):
    color = forms.BooleanField(required=False)
    pattern = forms.BooleanField(required=False)
    material = forms.BooleanField(required=False)
    price = forms.BooleanField(required=False)