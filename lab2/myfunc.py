import time
import os


def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i,k,j=0,0,0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i+=1
            else:
                alist[k]=righthalf[j]
                j+=1
            k+=1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i+=1
            k+=1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j+=1
            k+=1



def merge10Massive():

    x = [20,70,300,600,800,1500,2000,2500,3000,5000]
    file = "templates/5.txt"
    y = []
    
    with open(file,'r') as fs:

        for i in range(10):

            a = list(map(float,fs.readline().split(",")))
            t1 = time.time()
            mergeSort(a)
            t = time.time() - t1
            y.append(t)
    return x,y
merge10Massive()