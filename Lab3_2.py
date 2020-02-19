def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]

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
