from django.shortcuts import render
from .forms import ChooseMas
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from django.template import RequestContext
from .myfunc import mergeSort, merge10Massive
from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components
from bokeh.resources import CDN
import random
import math



def laboratory2(request):
    form = ChooseMas(request.POST or None)
    templ = {"form" : form}
    return render(request, "lab2.html", templ)

def lab2_exec(request):
    if request.POST:
        templ = {}

        if request.POST['Yours_list'] != '':
            your_list = list(map(int,request.POST['Yours_list'].split(",")))    
            mergeSort(your_list)
            answer = str(your_list)
            templ['answer'] = answer


        if 'Random_list' in request.POST.keys() and request.POST['Yours_list'] == '':
            rand_list = [random.randint(0,100) for i in range(random.randint(0,100))]
            mergeSort(rand_list)
            rand_list = str(rand_list)
            templ['answer'] = rand_list


        if 'Experiment' in request.POST.keys():

            x,y = merge10Massive()
            y1 = [i*math.log(i) for i in x]
        
            koef = sum([y[i]/y1[i] for i in range(len(y1))])/len(y1)
            y1 = list(map(lambda x: x*koef,y1))

            title = 'Experimental Data'

            plot = figure(title= title , 
            x_axis_label= 'N(numbers)', 
            y_axis_label= 'Time(T)', 
            plot_width =700,
            plot_height =400)

            plot.line(x, y,line_width = 3, line_color = "red")
            plot.line(x, y1,line_width = 3, line_color = "green")
            script, div = components(plot)

            cdn_js=CDN.js_files[0]
            cdn_css=CDN.css_files[0]

            templ['script'] = script
            templ['div'] = div
            templ['cdn_js'] = cdn_js
            templ['cdn_css'] = cdn_css
        
        return render(request, "lab2_plot.html", templ)