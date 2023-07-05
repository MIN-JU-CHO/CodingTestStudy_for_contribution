from collections import deque

N, M = map(int, input().split())
targets = list(map(int, input().split()))

queue = deque(list(range(1, N + 1)))
cnt = 0

for t in targets:
  while queue[0] != t:
    mid = len(queue) // 2
    if mid >= queue.index(t): # 찾아낼 값이 중간보다 왼쪽에 있을 때
      while queue[0] != t:
        queue.rotate(-1)
        cnt += 1
    else: # 찾아낼 값이 오른쪽에 있을 때
      while queue[0] != t:
        queue.rotate(1)
        cnt += 1
  queue.popleft()

print(cnt)
