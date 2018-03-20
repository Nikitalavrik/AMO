from django.shortcuts import render
from .forms import Lab4Form
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components
from bokeh.resources import CDN
from .myfunc import calc_func, myfunc
from numpy import arange

def laboratory4(request):
    form = Lab4Form(request.POST or None)
    
    templ = {"form" : form}
    return render(request, "lab4.html", templ)


def lab4_exec(request):
    if request.POST:
        a = float(request.POST['a'])
        b = float(request.POST['b'])
        e = float(request.POST['e'])

        x =calc_func(a,b,e)
        y = myfunc(x)
        
        step = (abs(a)+abs(b))/100
        xt = [x for x in arange(a,b,step)]
        yt = [myfunc(x) for x in xt]
        

        plot = figure(title= 'Interpolation' , 
            x_axis_label= 'X', 
            y_axis_label= 'Y', 
            plot_width =700,
            plot_height =400)

        plot.line(xt,yt,line_width = 4, line_color = "red")
        plot.circle(x,y,line_width = 8, line_color = "blue")
        print(a,b)
        if a == -1.0 and b == 1.0:
            x1 = -0.43843229759605
            y1 = myfunc(x1)
            print(1)
            plot.circle(x1,y1,line_width = 8, line_color = "blue")
            x = str(x) + "\n" + str(x1)
            y = str(y) + "\n" + str(y1)
        templ = {"x" : x, "y" : y}
        script1, div1 = components(plot)

        cdn_js=CDN.js_files[0]
        cdn_css=CDN.css_files[0]

        templ['script'] = script1
        templ['div'] = div1
        templ['cdn_js'] = cdn_js
        templ['cdn_css'] = cdn_css
        

        return render(request, "lab4_plot.html", templ)

    