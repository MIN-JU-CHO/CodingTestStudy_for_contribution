# 소요 시간: 56m (2차원 DP)
# 풀이: 
# 참고여부: 풀이 원리만 참고

# 2차원 DP를 이용한 방법
import sys

def input():
  return sys.stdin.readline().rstrip()

A = input()
B = input()

dp = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]
for b in range(1, len(B) + 1):  # 열
  for a in range(1, len(A) + 1):  # 행
    if B[b - 1] == A[a - 1]:
      dp[a][b] = dp[a - 1][b - 1] + 1
    else:
      dp[a][b] = max(dp[a][b - 1], dp[a - 1][b])

print(dp[-1][-1])
