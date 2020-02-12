from datetime import datetime as dt

def binary_search(arr, l, h, key):
    if l > h:
        return -1
    mid = (l + h) // 2
    if arr[mid] == key:
        return mid
    return binary_search(arr, mid+1, h, key) \
        if arr[mid] < key \
        else binary_search(arr, l, mid-1, key)

def linear_search(arr, i, key):
    if i == len(arr):
        return -1
    if arr[i] == key:
        return i
    else:
        return linear_search(arr, i+1, key)

def get_input():
    n = int(input("Enter number of elements: "))
    l = list()
    for i in range(n):
        l.append(int(input(f"Enter element {i}:")))
    return l

while True:
    choice = input(
        "Enter your choice:\n1. Binary search\n2. Linear search\n3. Exit\n"
    )
    if choice == '1' or choice == '2':
        l = get_input()
        key = int(input("Enter element to find: "))
        start = dt.now()
        loc = binary_search(l, 0, len(l) - 1, key) if choice == '1' else linear_search(l, 0, key)
        time = dt.now() - start
        print(f"Time taken: {time}")
        print("Element not found") \
            if loc == -1 \
            else print(f"Element found at position {loc}")
    else:
        break

