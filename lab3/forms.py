from django import forms



class Lab3Form(forms.Form):
    func = forms.BooleanField(label='cos(2*x + x**2)',required=False)
    Graph = forms.BooleanField(required = False)
    From_file = forms.BooleanField(required=False)
    file = forms.FileField(required=False)