import math
import random

file = "templates/lab3.txt"
x = [i*0.1 for i in range(100)]
y = [math.exp(math.sin(i)) for i in x]
x = str(x)
y = str(y)
with open(file, 'w') as f:
    f.write(x[1:len(x)-1] + '\n' + y[1:len(y)-1])



