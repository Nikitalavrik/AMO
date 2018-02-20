from django.shortcuts import render
from .forms import Part1,Part2,Part3
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from django.template import RequestContext
import math
import os

def laboratory1(request):

    form1 = Part1(request.POST or None)
    form2 = Part2(request.POST or None)
    form3 = Part3(request.POST or None)

    templ = {"form1" : form1, "form2" : form2, "form3" : form3}

    return render(request, "lab1.html",templ)

def part1(request):
    if request.POST:
        b = float(request.POST['b'])
        c = float(request.POST['c'])

        Y1 = 2*math.cos(b*c/2) + 2*math.sin(c*b/2)
        return HttpResponse(round(Y1,5))

    return render_to_response('lab1', RequestContext(request))

def part2(request):
    if request.POST:
        d = float(request.POST['d'])
        b = float(request.POST['b'])
        k = float(request.POST['k'])
        j = float(request.POST['j'])
        g = float(request.POST['g'])
        f = float(request.POST['f'])
        v = float(request.POST['v'])
        c = float(request.POST['c'])
        try:
            Y2 = math.sqrt((d-b-k*j)/(23*math.sqrt(g*f) + 6*math.sqrt(v*c)))
            Y2 = round(Y2,5)
        except:
            Y2 = "SQRT < 0 or denominator = 0"
        return HttpResponse(Y2)

    return render_to_response('lab1', RequestContext(request))

def part3(request):
    if request.POST:
        check = request.POST['fromFile']
        print(os.listdir())
        if check == 'on':
            file = "templates/4.txt"
            with open(file,'r') as fs:
                a = list(map(float,fs.readline().split(",")))
                c = list(map(float,fs.readline().split(",")))
                f = list(map(float,fs.readline().split(",")))
                g = list(map(float,fs.readline().split(",")))
        else:

            a = request.POST['a'].split(",")
            c = request.POST['c'].split(",")
            f = request.POST['f'].split(",")
            g = request.POST['g'].split(",")
        
        try:
            Y3 = 0
            for i in range(50):
                Y3 += a[i]**2 +56*c[i]*math.sqrt(f[i]*g[i])

            Y3 = round(Y3,5)
        except:
            Y3 = "length of values not equal or SQRT < 0"
        return HttpResponse(Y3)

    return render_to_response('lab1', RequestContext(request))