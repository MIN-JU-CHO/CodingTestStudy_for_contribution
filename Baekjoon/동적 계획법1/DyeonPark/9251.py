# 소요 시간: 56m (2차원 DP)
# 풀이: https://thinking-developer.tistory.com/173
# 참고여부: 풀이 원리만 참고

# (방식 1) 2차원 DP를 이용한 방법
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

# (방식 2) 누적합 방식
import sys

def input():
  return sys.stdin.readline().rstrip()

A = input()
B = input()
acc_sum = [0] * len(A)

for b in range(len(B)):
  cnt = 0
  for a in range(len(A)):
    # 먼저 같은지 비교하면 같은 글자가 연속으로 나왔을 때 카운팅이 안됨
    # 반례
    # ex1. XXXXXF / XFXXXQ
    # ex2. AAAY / YAAA
    # if A[a] == B[b]:
    #   acc_sum[a] = cnt + 1
    # else:
    #   cnt = max(cnt, acc_sum[a])
    if cnt < acc_sum[a]:
      cnt = acc_sum[a]
    elif A[a] == B[b]:
      acc_sum[a] = cnt + 1
      
print(max(acc_sum))
