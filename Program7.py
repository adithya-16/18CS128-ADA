from math import factorial 

class DirNum:
    def __init__(self, num):
        self.num = num
        self.dir = -1 # right to left 
    
    def changeDir(self):
        self.dir = -self.dir 

    def __gt__(self, other):
        return self.num > other.num

n = int(input("Enter n: "))
nums = [DirNum(i) for i in range(1, n + 1)]

# print 1st perumtation
for dirNum in nums:
    print(dirNum.num, end=' ')
print()


def getMobile(nums):
    mobile = DirNum(0) 

    for i in range(len(nums)):
        dirNum = nums[i]
        if (dirNum.dir == -1 and i != 0) or (dirNum.dir == 1 and i < len(nums) - 1): # (right to left) or (left to right) 
            if dirNum > nums[i + dirNum.dir] and dirNum > mobile:
                mobile = dirNum
    
    return mobile


def printOnePerm(nums):
    mobile = getMobile(nums)
    index = nums.index(mobile)

    # swap number in mobile dir
    nums[index], nums[index + mobile.dir] = nums[index + mobile.dir], nums[index]

    # change dir and print at the same time
    for dirNum in nums:
        if dirNum > mobile:
            dirNum.changeDir()
        print(dirNum.num, end=' ')
    print()


for i in range(factorial(n) - 1):
    printOnePerm(nums)

#edit distance

str1 = input('Enter string 1: ')
str2 = input('Enter string 2: ')

def findEditDistance(str1, str2):
    if not str1:
        return len(str2) 
    elif not str2:
        return len(str1)

    if str1[-1] == str2[-1]:
        return findEditDistance(str1[:-1], str2[:-1])
    
    return 1 + min(findEditDistance(str1[:-1], str2[:-1]), 
                   findEditDistance(str1, str2[:-1]), 
                   findEditDistance(str1[:-1], str2))

print(findEditDistance(str1, str2))