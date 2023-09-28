# 소요 시간: 25m
# 풀이: https://thinking-developer.tistory.com/172
# 참고여부: 풀이 원리만 참고

import sys

def input():
  return sys.stdin.readline().rstrip()

N = int(input())
DIV = 1000000000

stairs = [[0] * 10 for i in range(N + 1)]

# 초기값 설정
for i in range(1, 10):
  stairs[1][i] = 1

# 계산
if N >= 2:
  for i in range(2, N + 1):
    for j in range(10):
      if j == 0:
        stairs[i][j] = stairs[i - 1][1]
      elif j == 9:
        stairs[i][j] = stairs[i - 1][8]
      else:
        stairs[i][j] = (stairs[i - 1][j - 1] + stairs[i - 1][j + 1])

# 답 출력
total = 0
for i in range(10):
  # print(f"[{N}][{i}]: {stairs[N][i]}")
  total += stairs[N][i]
print(total % DIV)
