def get_permutations(n):
    digits = list(range(1,n+1))
    dir = [ True for i in range(n) ]
    k = get_mobile(digits, dir)
    while k != -1:

        k = get_mobile(digits, dir)
        string = ''
        for digit in digits:
            string += str(digit)
        print(string)
        if dir[k] and digits[k-1] < digits[k]:
            print(k, dir[k], digits[k])
            digits[k], digits[k-1] = digits[k-1], digits[k]
            dir[k], dir[k-1] = dir[k-1], dir[k]
            for i in range(len(digits)):
                if digits[k-1] < digits[i]:
                    dir[i] = not dir[i]
        elif not dir[k] and digits[k+1] < digits[k]:
            print("here2")
            digits[k], digits[k+1] = digits[k+1], digits[k]
            for i in range(len(digits)):
                if digits[k+1] < digits[i]:
                    dir[i] = not dir[i]
    
def get_mobile(digits, dir):
    # prev = digits.index(max(digits))
    # if (prev != len(digits)-1 and not dir[prev]) or (prev != 0 and dir[prev]):
    #     return prev
    prev = 0
    check = False
    for i in range(len(digits)):
        if (i != len(digits) - 1 and not dir[i]) or (i != 0 and dir[i]):
            check = True
            if digits[i] > digits[prev]:
                prev = i
    return prev if check else -1

get_permutations(4)