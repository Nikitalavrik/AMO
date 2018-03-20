from math import cos,pi,sin
#x^2-cos(pi*x)=0

myfunc = lambda x: x**2 - cos(pi*x)
myfuncder1 = lambda x: 2*x + pi*sin(pi*x)
myfuncder2 =lambda x: 2 + pi**2 * cos(pi*x)

def calc_func(a,b,e):
    x = a
    if myfunc(x)*myfuncder2(x) < 0:
        x = b
        if myfunc(x)*myfuncder1(x) < 0:
            return "Error"

    while True:
        
        x1 = x - myfunc(x)/myfuncder1(x)
        if abs(x1 - x)<e:
            return x
        else:
            x = x1

