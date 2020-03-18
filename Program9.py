from matplotlib import pyplot
from datetime import datetime as dt
import random as r

def partition(arr,low,high): 
    i = ( low-1 )
    pivot = arr[high]
  
    for j in range(low , high): 
        if   arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
 
def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
        
def findGrid(n):  
    arr = [[0 for k in range(n)] for l in range(n)]  
    x = 0
    for i in range(n // 4):  
        for j in range(n // 4):  
            for k in range(4):  
                for l in range(4):  
                    arr[i * 4 + k][j * 4 + l] = x  
                    x += 1
    for i in range(n):  
        for j in range(n):  
            print(arr[i][j], end = " ") 
        print() 
  
n = 4
findGrid(n)  

def plot():
  x = []
  y = []
  for i in range(1,1002,20):
    print(i)
    arr = [ r.randint(0,1000) for j in range(i) ]
    start = dt.now()
    quick_sort(arr)
    t = dt.now() - start
    x.append(i)
    y.append(float(str(t.total_seconds())))
  pyplot.plot(x, y)
  pyplot.xlabel('N')
  pyplot.ylabel('Time (seconds)')
  pyplot.grid()
  pyplot.savefig("time.png")

plot()
