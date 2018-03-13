import math
from functools import reduce



multi = lambda a: reduce(lambda x,y: x*y, a)

def lagrange(x, xp, fp):

  l = lambda m: multi((x - xp[n])/(xp[m] - xp[n]) for n in range(len(xp)) if n != m)


  return sum([fp[m]*l(m) for m in range(len(xp))])


class Interpolation:

  def __init__(self, *args, **kwargs):
  
    self.xarr = [round(x*0.1,2) for x in range(10)]
    self.y = [math.cos(2*x+x**2) for x in self.xarr]
    self.output = [self.lagran(x,self.xarr,self.y) for x in self.xarr]


  def lagran(self, x, xarr, y):

    polinom = []
    for i in range(len(xarr)):
      polinom.append(reduce(lambda x,y: x*y,[(x - xarr[k])/(xarr[i] - xarr[k]) for k in range(len(xarr)) if k != i]) *y[i])
    output = sum(polinom)

    return output

  def newton(self, x, xarr, y): 
    ln = sum([self.a_i(i,xarr,y)*multi((x-xarr[n-1]) for n in range(1,i+1)) for i in range(1,len(xarr)) ])
    ln += y[0]
    return ln
  
  def a_i(self, param, xarr, y):
    a = 0
    for i in range(param+1):
      a += y[i]/multi((xarr[i]-xarr[n]) for n in range(param+1) if i != n)
    return a

  def neville(self, x, xarr, fp):
    n = len(xarr)
    p = n*[0]
    for k in range(n):
        for i in range(n - k):
            if k == 0:
                p[i] = fp[i]
            else:
                p[i] = ((x - xarr[i + k])*p[i] + (xarr[i] - x)*p[i+1])/(xarr[i] - xarr[i + k])
    return p[0]


  def flat(self, func, x, xarr, y,n):
    l = []
    #for i in range(2,12):
     # n1 = func(x,xarr[0:i],y[0:i]) - func(x,xarr[0:i+1],y[0:i+1])
     # l.append(- math.log(abs(n1),10) if n1 != 0 else n1)
    for j in range(2,n):
      
      x = (x-j*math.pi/(2*n))/((j+1)*math.pi/(2*n) - j*math.pi/(2*n))
      n1 = func(x,xarr[0:j],y[0:j]) - func(x,xarr[0:j+1],y[0:j+1])
      l.append(- math.log(abs(n1),10) if n1 != 0 else n1)

    return l
