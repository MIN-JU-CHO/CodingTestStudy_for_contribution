# https://thinking-developer.tistory.com/165
# 첫 번째 풀이 (Brute-force)
import sys
from itertools import combinations, permutations

input = sys.stdin.readline

N = int(input())
powers = [list(map(int, input().split())) for _ in range(N)]

team_num = N // 2
members = set(range(N))
minimum = sys.maxsize

teams = combinations(members, team_num)
for mem in teams:
  A = set(mem)
  B = members-A

  sum_A = 0
  sum_B = 0
  
  for p in permutations(A, 2):
    sum_A += powers[p[0]][p[1]]
  for p in permutations(B, 2):
    sum_B += powers[p[0]][p[1]]

  minimum = min(minimum, abs(sum_A-sum_B))

print(minimum)


# 두 번째 풀이 (Backtracking)
import sys
input = sys.stdin.readline

N = int(input())
powers = [list(map(int, input().split())) for _ in range(N)]

members = [False] * N
minimum = sys.maxsize

def backtracking(depth: int, mem_idx: int):
  global minimum
  if depth == (N // 2):
    sum_A, sum_B = 0, 0
    for i in range(N):
      for j in range(N):
        if members[i] and members[j]:
          sum_A += powers[i][j]
        elif not members[i] and not members[j]:
          sum_B += powers[i][j]

    minimum = min(minimum, abs(sum_A - sum_B))
  else:
    for i in range(mem_idx, N):
      if not members[i]:
        members[i] = True
        backtracking(depth + 1, i + 1)
        members[i] = False
  
backtracking(0, 0)
print(minimum)
