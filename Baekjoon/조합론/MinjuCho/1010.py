# 다이나믹 프로그래밍
# Memoization list
d=[0] * 31

# 팩토리얼 함수
def factorial(n):
    if n==1 or n==0:
        return 1
    elif d[n]!=0:
        return d[n]
    else:
        d[n] = n*factorial(n-1)
        return d[n]

# 입력 받기
T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    # mCn 계산하여 출력하기
    print(int(factorial(M)/(factorial(M-N)*factorial(N))))
