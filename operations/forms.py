from django import forms

class EmiForm(forms.Form):

    amount=forms.IntegerField()

    interest=forms.IntegerField()

    tenure=forms.IntegerField()

class TempartureForm(forms.Form):

    temp_in_deg=forms.IntegerField(required=False)
    
    temp_in_fh=forms.IntegerField(required=False)