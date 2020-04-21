n_vertices = int(input('Enter number of vertices: '))
adj_wt_mat = [[0] * n_vertices] * n_vertices
for i in range(n_vertices):
    adj_wt_mat[i] = list(map(int, input().split()))

d = adj_wt_mat.copy()
for k in range(n_vertices):
    for i in range(n_vertices):
        for j in range(n_vertices):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

print(d)

arr = list(map(int, input("enter array of numbers: ").split()))

# pythonic way    
sumEvenBitDigits = sum([digit for digit in arr if bin(digit)[2:].count('1') % 2 == 0])
print(sumEvenBitDigits)

# normal way
def isEven1Bits(num):
    one_count = 0
    while num:
        one_count += num & 1
        num >>= 1
    return one_count % 2 == 0

sumEvenBitDigits = 0
for digit in arr:
    if isEven1Bits(digit):
        sumEvenBitDigits += digit
print(sumEvenBitDigits)