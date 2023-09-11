# 풀이 생각 및 시도 : 1시간 -> failes (RuntimeError)

# 1차 시도 풀이
# 새로 들어온 전기줄과 기존에 있던 전기줄을 비교한다
# 이 때 새로 들어온 전기줄의 시작줄이 비교하는 기존 전기줄보다 숫자가 크거나 작았으면, 도착하는 지점의 숫자도 같은 대소 비교와 같이 크거나 작아야 한다
# 이를 어기는 경우가 발생한다면, 전기줄의 길이를 계산하여 길이가 긴 쪽을 삭제하도록 한다
import sys

def input():
  return sys.stdin.readline().rstrip()

N = int(input())
lines = [tuple(map(int, input().split()))]

cnt = 0
for _ in range(N - 1):
  del_list = []
  left, right = tuple(map(int, input().split()))

  new_value_collision = False
  for idx, val in enumerate(lines):
    if (left > val[0] and right < val[1]) or (left < val[0] and right > val[1]):
      if abs(left - right) >= abs(val[0] - val[1]):
        new_value_collision = True
        cnt += 1
        break
      else: 
        del_list.append(idx)

  for i in del_list:
    del lines[i]
    cnt += 1

  if not new_value_collision:
    lines.append((left, right))

print(cnt)

# 2차 풀이 (참고: https://hongcoding.tistory.com/157)
# 전기줄이 교차하지 않는 조건을 찾는다. 이는 다음과 같다
# 1) 전기줄의 왼쪽 번호가 작은 순서대로 정렬을 한다
# 2) 다음 전기줄의 오른쪽 번호가 이전 전기줄의 오른쪽 번호보다 크거나 같아야 한다
# 3) 즉, 앞 전기줄의 오른쪽 번호가 뒷 전기줄의 오른쪽 번호보다 작은 경우가 최대로 이어지는 경우를 찾는다

import sys

def input():
  return sys.stdin.readline().rstrip()

N = int(input())
lines = [tuple(map(int, input().split())) for i in range(N)]
dp = [1] * N

lines.sort()

for i in range(1, N):
  for j in range(0, i):
    if lines[j][1] < lines[i][1]:
      dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
