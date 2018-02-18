import random


file = "4.txt"

with open(file,"w") as f:
    for i in range(4):
        inp = str([random.randint(0,100) for i in range(50)])
        f.writelines(inp[1:len(inp)-1] + '\n')
