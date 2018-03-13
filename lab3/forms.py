from django import forms



class Lab3Form(forms.Form):
    lagrange = forms.BooleanField(required = False)
    Newton = forms.BooleanField(required = False)
    eitken = forms.BooleanField(required = False)
    Graph = forms.BooleanField(required = False)
