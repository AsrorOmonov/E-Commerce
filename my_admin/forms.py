from django import forms

from my_admin.models import OutfitModel


class OutfitModelForm(forms.ModelForm):
    class Meta:
        model = OutfitModel
        exclude = ['created_at']
