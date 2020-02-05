def binary_search(arr, key):
    low = 0
    high = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif key > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def count(arr, key, loc):
    if loc == -1:
        return 0
    count = 0
    i = loc
    while arr[i] == key:
        count +=1
        i -= 1
    i = loc + 1
    while i != len(arr) and arr[i] == key:
        count += 1
        i += 1
    return count

def first(arr, key, loc):
    if loc == -1:
        return -1
    if arr[0] == key:
        return 0
    low = 0
    high = loc
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key and arr[mid-1] < key:
            return mid
        elif arr[mid] > key:
            low = mid + 1
        else:
            high = mid - 1
    return loc

def last(arr, key, loc):
    if loc == -1:
        return -1
    if arr[-1] == key:
        return len(arr) - 1
    low = loc
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key and arr[mid+1] > key:
            return mid
        elif arr[mid] > key:
            low = mid + 1
        else:
            high = mid - 1
    return loc
    
arr = [ 2, 2, 8, 12, 12, 12, 12, 12 ]
loc = binary_search(arr, 12)
print(count(arr, 12, loc))
print(first(arr, 12, loc))
print(last(arr, 12, loc))