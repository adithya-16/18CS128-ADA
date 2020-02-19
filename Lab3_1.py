from matplotlib import pyplot
from datetime import datetime as dt
import random as r

def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]

def plot():
  x = []
  y = []
  for i in range(1,1002,20):
    arr = [ r.randint(0,1000) for j in range(i) ]
    start = dt.now()
    selection_sort(arr)
    t = dt.now() - start
    x.append(i)
    y.append(float(str(t.total_seconds())))
  pyplot.plot(x, y)
  pyplot.xlabel('N')
  pyplot.ylabel('Time (seconds)')
  pyplot.grid()
  pyplot.savefig("time.png")

plot()
