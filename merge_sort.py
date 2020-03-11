from matplotlib import pyplot
from datetime import datetime as dt
import random as r

def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    l = arr[:mid]
    r = arr[mid:]
    merge_sort(l)
    merge_sort(r)
    i = j = k = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j+=1
        k += 1

    while i < len(l): 
        arr[k] = l[i] 
        i+=1
        k+=1
          
    while j < len(r): 
        arr[k] = r[j] 
        j+=1
        k+=1

def plot():
  x = []
  y = []
  for i in range(1,1002,20):
    print(i)
    arr = [ r.randint(0,1000) for j in range(i) ]
    start = dt.now()
    merge_sort(arr)
    t = dt.now() - start
    x.append(i)
    y.append(float(str(t.total_seconds())))
  pyplot.plot(x, y)
  pyplot.xlabel('N')
  pyplot.ylabel('Time (seconds)')
  pyplot.grid()
  pyplot.savefig("time.png")

plot()
