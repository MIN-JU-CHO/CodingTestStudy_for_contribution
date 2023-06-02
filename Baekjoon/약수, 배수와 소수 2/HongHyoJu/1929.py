import math


def is_Prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(num)+1)):
            if num % i == 0:
                return False
        return True


M, N = map(int, input().split())

for i in range(M, N+1):
    if is_Prime(i):
        print(i)
