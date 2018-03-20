from django.shortcuts import render
from .forms import Lab3Form
from .interpolation import lagrange,Interpolation
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
        xt = [round(x*0.01,3) for x in range(100)]
        fpt = [math.cos(2*x+x**2) for x in xt]

        xp = [round(x*0.1,2) for x in range(12)]
        fp = [math.cos(2*x+x**2) for x in xp]
        inter = Interpolation()
        fpn, fpl, fpe = None, None, None

        if 'lagrange' in request.POST.keys():

            fpl = [lagrange(x,xp[0:10],fp[0:10]) for x in xp[0:10]]
            fplt = [lagrange(x,xt,fpt) for x in xt]
            lagran_flat = [inter.flat(lagrange,x,xp,fp,10) for x in xp]
            templ['lagrange'] ="Lagrange : " +  str(fpl[:3])

        if 'Newton' in request.POST.keys():
            
            fpn = [Interpolation().newton(x,xp[0:10],fp[0:10]) for x in xp[0:10]]
            newton_flat = [inter.flat(inter.newton,x,xp,fp,10) for x in xp]    
            templ['newton'] ="Newton : " + str(fpn)

        if 'eitken' in request.POST.keys():
            
            fpe = [Interpolation().neville(x,xp[0:10],fp[0:10]) for x in xp[0:10]]    
            eitken_flat = [inter.flat(inter.neville,x,xp,fp,10) for x in xp]   
            templ['eitken'] = "Eitken : " + str(fpe)

        if 'Graph' in request.POST.keys() and any([fpl,fpn,fpe]):

            plot = figure(title= 'Interpolation' , 
            x_axis_label= 'X', 
            y_axis_label= 'Y', 
            plot_width =700,
            plot_height =400)



            if fpl:
                plot.line(xt[::10], fplt[::10],line_width = 4, line_color = "red")
                script2,div2 = generate_plot("Lagrange Flat",xp,lagran_flat)
                templ['script2'] = script2
                templ['div2'] = div2
            if fpn:
                print()
                plot.line(xp[:10:2], fpn[:10:2],line_width = 3, line_color = "green")
                script3,div3 = generate_plot("Newton Flat",xp,newton_flat)
                templ['script3'] = script3
                templ['div3'] = div3
            if fpe:
                
                plot.line(xp[:10:2], fpe[:10:2],line_width = 1, line_color = "blue")
                script4,div4 = generate_plot("Eitken Flat",xp,eitken_flat)
                templ['script4'] = script4
                templ['div4'] = div4

            script1, div1 = components(plot)

            cdn_js=CDN.js_files[0]
            cdn_css=CDN.css_files[0]

            templ['script1'] = script1
            templ['div1'] = div1
            templ['cdn_js'] = cdn_js
            templ['cdn_css'] = cdn_css

    return render(request,'lab3_plot.html',templ)

def generate_plot(title,xp,y):
    plot = figure(title= title , 
                    x_axis_label= 'X', 
                    y_axis_label= 'Y', 
                    plot_width =700,
                    plot_height =400)
    colors = ["red","green","black","pink","blue","orange","purple","grey","yellow","white","brown","green"]
    for i in range(len(y)):
        plot.line(xp[:8], y[i],line_width = 2, line_color = colors[i])

    return components(plot)