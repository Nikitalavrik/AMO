from django import forms


class Part1(forms.Form):
    b = forms.FloatField()
    c = forms.FloatField()
    fromFile = forms.BooleanField()
    file = forms.FileField(required = False)

class Part2(forms.Form):
    d = forms.FloatField()
    b = forms.FloatField()
    k = forms.FloatField()
    j = forms.FloatField()
    g = forms.FloatField()
    f = forms.FloatField()
    v = forms.FloatField()
    c = forms.FloatField()
    fromFile = forms.BooleanField()
    file = forms.FileField(required = False)

class Part3(forms.Form):
    a = forms.CharField(required = False)
    c = forms.CharField(required = False)
    f = forms.CharField(required = False)
    g = forms.CharField(required = False)
    fromFile = forms.BooleanField()
    file = forms.FileField(required = False)