import math

M = int(input())
N = int(input())
# M <= N


def is_Prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True


arr = []
for i in range(M, N+1):
    if is_Prime(i):
        arr.append(i)

print(sum(arr))
print(min(arr))
