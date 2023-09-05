# for 문 이용 및 수학계산에 따른 접근 : 시간 초과 풀이
import math

N = int(input())

res = []
for i in range((N // 2) + 1):
  if i == 0:
    res.append(1)
  else:
    res.append(math.comb(N - i, i))

print(sum(res) % 15746)


# DP 풀이
N = int(input())

MAX = 1000000
res = [0] * (MAX + 1)

res[1] = 1
res[2] = 2

for i in range(3, MAX + 1):
  # 바로 나눠주지 않으면 메모리 초과 에러가 뜸 (정수로 표현할 수 있는 수의 한계로 인한 것으로 추정
  res[i] = (res[i - 2] + res[i - 1]) % 15746

print(res[N])
