import sys
input = sys.stdin.readline
N = int(input())
dt = [0] + list(map(int,input().split())) + [0]

LIS = [0] * (N+2)
LISR = [0] * (N+2)

# 왼쪽 기준 누적 순위 구하기
for i in range(1, N+1):
    for j in range(0, i):
        if dt[j] < dt[i]:
            LIS[i] = max(LIS[i] , LIS[j] + 1)

# 오른쪽 기준 누적 순위 구하기
for i in range(N+1, 0, -1):
    for j in range(N+1, i, -1):
        if dt[i] > dt[j]:
            LISR[i] = max(LISR[i] , LISR[j] + 1)

# LR 더해서 가장 큰 값이 가장 긴 바이토닉 길이
for i in range(N+2):
    LIS[i] += LISR[i]

# 자기 자신 원소 중복 빼기
print(max(LIS)-1)
