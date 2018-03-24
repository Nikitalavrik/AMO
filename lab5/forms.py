from django import forms


class Lab5Form(forms.Form):
    row = forms.IntegerField(max_value=10)
