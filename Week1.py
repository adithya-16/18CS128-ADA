def euclid(m, n):
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m

def cic(m, n):
    smallest = min(m,n)
    while not (m % smallest == 0 and n % smallest == 0):
        smallest -= 1
    return smallest

def rec(m, n):
    return rec(n, m % n) if n != 0 else m

def toh(n,from_rod,to_rod,aux_rod):
    if n == 1:
        print(f"Moved disc 1 from {from_rod} to {to_rod}.")
        return
    toh(n-1,from_rod,aux_rod,to_rod)
    print(f"Moved disc {n} from {from_rod} to {to_rod}")
    toh(n-1,aux_rod,to_rod,from_rod)


while True:
    choice = int(
        input(
            """
            Enter your choice:
            1. GCD by Euclid's method
            2. GCD by Consecutive Integer Checking Method
            3. GCD by Recursive Modulus method
            4. Tower of Hanoi
            5. Exit
            """
        )
    )
    if choice in range(1,4):
        m = int(
            input("Enter m: ")
        )
        n = int(
            input("Enter n: ")
        )
        m1 = max(m,n)
        n1 = min(m,n)
        res = -1
        if m1 < 1 or n1 < 1:
            print("Invalid input.")
        elif choice == 1:
            res = euclid(m1, n1)
        elif choice == 2:
            res = cic(m1, n1)
        else:
            res = rec(m1, n1)
        print(f"GCD of {m} and {n} is {res}.")
    elif choice == 4:
        toh(4, 'A', 'C', 'B')
    else:
        break

        