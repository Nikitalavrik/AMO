from django.shortcuts import render
from .forms import Lab3Form
from .lagran import lagrange
from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components
from bokeh.resources import CDN
import math

def laboratory3(request):
    form = Lab3Form(request.POST or None)
    templ = {"form" : form}
    return render(request, "lab3.html", templ)

def lab3_exec(request):
    if request.POST:
        
        templ = {}

        if 'func' in request.POST.keys():
            xp = [round(x*0.1,2) for x in range(10)]
            fp = [math.cos(2*x+x**2) for x in xp]
            fpl = [lagrange(x,xp,fp) for x in xp]
            templ['func'] = 'y = cos(2*x + x**2)'
            templ['notanswer'] = str(fp)
            templ['answer'] = str(fpl)

        if 'From_file' in request.POST.keys():
            with open('templates/lab3.txt', 'r') as f:
                xp = list(map(float,f.readline().split(",")))
                fp = list(map(float,f.readline().split(",")))
                fpl = [lagrange(x,xp,fp) for x in xp]
                templ['func'] = 'UNKNOW'
                templ['notanswer'] = str(fp)
                templ['answer'] = str(fpl)                

        if 'Graph' in request.POST.keys() and xp:

            title = 'Experimental Data'

            plot = figure(title= title , 
            x_axis_label= 'X', 
            y_axis_label= 'Y', 
            plot_width =700,
            plot_height =400)

            x = xp[::2]
            fpl = fpl[::2]
            plot.line(xp, fp,line_width = 3, line_color = "red")
            plot.line(x, fpl,line_width = 2, line_color = "green")

            script, div = components(plot)

            cdn_js=CDN.js_files[0]
            cdn_css=CDN.css_files[0]

            templ['script'] = script
            templ['div'] = div
            templ['cdn_js'] = cdn_js
            templ['cdn_css'] = cdn_css

    return render(request,'lab3_plot.html',templ)   