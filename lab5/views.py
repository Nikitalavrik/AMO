from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components
from bokeh.resources import CDN
from .forms import Lab5Form

def laboratory5(request):
    form = Lab5Form(request.POST or None)
    
    templ = {"form" : form}
    return render(request, "lab5.html",templ)

def lab5_exec(request):
    if request.POST:
        row = [0]*int(request.POST['row'])
        enter_matrix = "Enter your matrix"

        templ = {"row" : row, "enter_matrix" : enter_matrix}

        return render(request, "lab5.html",templ)