# 문제 해설 https://velog.io/@cuppizza/11866-%EC%9A%94%EC%84%B8%ED%91%B8%EC%8A%A4-%EB%AC%B8%EC%A0%9C-0
from collections import deque
N, K = map(int, input().split())
# [1, 2, 3, ... , N]
queue = [ i for i in range(1, N+1) ]
queue = deque(queue)
result = []
for _ in range(N):
    for time in range(K-1):
        # 큐의 원소들을 왼쪽으로 한 칸씩 이동
        queue.append(queue.popleft())
    # K번째 차례에서 맨 왼쪽 원소 뽑기
    result.append(queue.popleft())
    
print("<", end="")
if len(result)==1:
    print(str(result[0])+">", end="")
else:
    for i in range(len(result)-1):
        print(str(result[i])+", ", end="")
    print(str(result[i+1])+">", end="")
