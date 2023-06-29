import sys 
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

people = [i for i in range(1, N + 1)]
queue = deque(people)

result = []
while len(queue) != 0:
  queue.rotate(-(K-1))
  result.append(str(queue.popleft()))

print(f"<{', '.join(result)}>")
