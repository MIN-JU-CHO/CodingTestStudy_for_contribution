# 소요 시간: 43m
# 풀이: https://thinking-developer.tistory.com/174
# 참고여부: 참고하지 않음

import sys
sys.setrecursionlimit(1000000)

def input():
  return sys.stdin.readline().rstrip()

N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]

blue_cnt = 0
white_cnt = 0

def divide_n_conquer(x: int, y: int, n: int):
  # 부분합 계산
  total = 0
  for i in range(n):
    total += sum(papers[x + i][y:y + n])

  # 부분합 값에 따른 판별
  if total == n**2:
    global blue_cnt
    blue_cnt += 1
    return
  elif total == 0:
    global white_cnt
    white_cnt += 1
    return
  else:
    half = n // 2
    divide_n_conquer(x, y, half)
    divide_n_conquer(x, y + half, half)
    divide_n_conquer(x + half, y, half)
    divide_n_conquer(x + half, y + half, half)

divide_n_conquer(0, 0, N)
print(f"{white_cnt}\n{blue_cnt}")
