arr = list(map(int, input("Enter elements: ").split(' ')))
key = int(input("Enter key"))

l, h = 0, len(arr)-1
first, last = 0, 0

def bin(arr, key, l, h):
    global first, last
    if l > h:
        return
    mid = (l + h) // 2
    if arr[mid] == key:
        if mid > 0 and arr[mid-1] == key:
            h = mid - 1
            first = h 
            bin(arr, key, l, h)
        if mid < len(arr)-1 and arr[mid+1] == key:
            l = mid + 1
            last = l
            bin(arr, key, l, h)
        else:
            return
    elif key > arr[mid]:
        l = mid + 1
    else:
        h = mid - 1
    bin(arr, key, l, h)

bin(arr, key, l, h)

print(f'First Occurrence: {first}')
print(f'Last Occurrence: {last}')
print(f'Number of Occurrences: {last-first+1}')