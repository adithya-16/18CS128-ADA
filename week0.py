print("__input__")
T = int(input())
res = list()

for i in range(T):
    params = input()
    N = int(params[0])
    K = int(params[2])
    array = input()
    arr = [int(ele) for ele in array.split(' ')]
    if K in arr:
        res.append(1)
    else:
        res.append(-1)

print("\n__output__")

for i in res:
    print(i)