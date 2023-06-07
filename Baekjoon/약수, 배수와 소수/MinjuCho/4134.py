import math
cases = int(input())

def is_prime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

for case in range(cases):
    N = int(input())
    find = N
    while True:
        if is_prime(find) == True:
            print(find)
            break
        else:
            find += 1
