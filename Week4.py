def insertion_sort(arr):
    for i in range(1,len(arr)):
        item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > item:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = item

l = [ 5, 3, 9 ,15, 2, 1, 40, 39 ]
insertion_sort(l)
print(l)

def meet_sort(arr):
    for i in range(1,len(arr)):
        item = arr[i]
        j = i - 1
        while j >= 0 and (arr[j][1] - arr[j][0]) > (item[1] - item[0]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = item
    for i in range(1,len(arr)):
        item = arr[i]
        j = i - 1
        while j >= 0 and arr[j][0] >= item[1]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = item

def count_meetings(m):
    meet_sort(m)
    print(m)
    count = 1
    print(f"Meeting 1: {m[0][0]}-{m[0][1]}")
    for i in range(1,len(m)):
        if not m[i-1][0] >= m[i][0]:
            count += 1
            print(f"Meeting {count}: {m[i][0]}-{m[i][1]}")
    print(f"There can be {count} meetings out of {len(m)} scheduled.")

m = [ [10,12], [10,11], [11, 12], [10,11], [21,22], [20,21], [12, 13], [19, 22], [8,9] ]
count_meetings(m)

        
            
