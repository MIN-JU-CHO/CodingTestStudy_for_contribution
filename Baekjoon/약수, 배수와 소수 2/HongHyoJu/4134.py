import math

# 임의의 양수 M이 sqrt(M) 보다 작거나 같은 약수를 가지지 않으면 소수이다.


def is_Prime(num):
    if num == 0 or num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True


arr = []
N = int(input())
for _ in range(N):
    num = int(input())
    while True:
        if is_Prime(num):
            arr.append(num)
            break
        else:
            num += 1

for i in range(N):
    print(arr[i])
