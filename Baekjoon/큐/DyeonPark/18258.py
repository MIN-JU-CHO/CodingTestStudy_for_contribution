import sys
from collections import deque

input = sys.stdin.readline

def isEmpty(nums):
  if len(nums) == 0:
    return 1
  else:
    return 0

queue = deque()
for _ in range(int(input())):
  cmd = list(input().split())
  if cmd[0] == "push":
    queue.append(int(cmd[1]))
  elif cmd[0] == "pop":
    if isEmpty(queue):
      print(-1)
    else:
      print(queue.popleft())
  elif cmd[0] == "front":
    if isEmpty(queue):
      print(-1)
    else:
      print(queue[0])
  elif cmd[0] == "back":
    if isEmpty(queue):
      print(-1)
    else:
      print(queue[-1])
  elif cmd[0] == "size":
    print(len(queue))
  elif cmd[0] == "empty":
    print(isEmpty(queue))
