import random


file = "5.txt"
x = [20,70,300,600,800,1500,2000,2500,3000,5000]

with open(file,"a") as f:
    for i in x:
        inp = str([random.randint(0,100) for j in range(i+1)])
        f.writelines(inp[1:len(inp)-1] + '\n')


