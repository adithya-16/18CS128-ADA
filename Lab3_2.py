def merge_sort(arr):
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
            arr[j] = r[j]
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

def k_largest():
    k = int(input("Enter k: "))
    n = int(input("Enter n: "))
    if k > n:
        print("Error")
        return
    l = [ int(input(f"Enter element {i}: ")) for i in range(n) ]
    selection_sort(l)
    for ele in l[::-1][:k]:
        print(f"{ele}",end=" ")

k_largest()    
