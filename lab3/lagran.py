import math
from functools import reduce

product = lambda a: reduce(lambda x,y: x*y, a)

def lagrange(x, xp, fp):

  l = lambda m: product((x - xp[n])/(xp[m] - xp[n]) for n in range(len(xp)) if n != m)


  return sum([fp[m]*l(m) for m in range(len(xp))])


