from datetime import datetime as dt

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

def get_input():
    n = int(input("Enter number of elements: "))
    l = list()
    for i in range(n):
        l.append(int(input(f"Enter element {i}:")))
    return l

while True:
    choice = input(
        "Enter your choice:\n1. Bubble sort\n2. Selection sort\n3. Exit"
    )
    if choice == '1' or choice == '2':
        l = get_input()
        start = dt.now()
        bubble_sort(l) if choice == '1' else selection_sort(l)
        time = dt.now() - start
        print(f"Time taken: {time}\nSorted array: ",l)
    else:
        break
