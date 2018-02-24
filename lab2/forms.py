from django import forms


class ChooseMas(forms.Form):
    Yours_list = forms.CharField(required = False)
    Random_list = forms.BooleanField(required = False)
    Experiment = forms.BooleanField(required = False)
    Fromfile = forms.BooleanField(required = False)
    
   
