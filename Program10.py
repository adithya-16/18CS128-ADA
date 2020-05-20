def heap(arr, n, i): 
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]: 
        largest = l t exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]
        heap(arr, n, largest) 
def heapSort(arr): 
    n = len(arr) 
    for i in range(n//2 - 1, -1, -1): 
        heap(arr, n, i) 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heap(arr, i, 0) 
arr1 = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr1) 
n = len(arr1) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" % arr1[i]), 


N = 5
ptr = [0 for i in range(501)] 
def findSmallestRange(arr, n, k): 
    i, minval, maxval, minrange, minel, maxel, flag, minind = 0, 0, 0, 0, 0, 0, 0, 0
    for i in range(k + 1): 
        ptr[i] = 0
    minrange = 10**9
    while(1):     
        minind = -1
        minval = 10**9
        maxval = -10**9
        flag = 0
        for i in range(k): 
            if(ptr[i] == n): 
                flag = 1    
                break
            if(ptr[i] < n and arr[i][ptr[i]] < minval): 
                minind = i # update the index of the list 
                minval = arr[i][ptr[i]]  
            if(ptr[i] < n and arr[i][ptr[i]] > maxval): 
                maxval = arr[i][ptr[i]] 
        if(flag): 
            break
        ptr[minind] += 1
        if((maxval-minval) < minrange): 
            minel = minval 
            maxel = maxval 
            minrange = maxel - minel 
      
    print("The smallest range is [", minel, maxel, "]") 

arr2 = [ 
    [4, 7, 9, 12, 15], 
    [0, 8, 10, 14, 20], 
    [6, 12, 16, 30, 50] 
    ] 
  
k = len(arr2) 
  
findSmallestRange(arr2, N, k) 
