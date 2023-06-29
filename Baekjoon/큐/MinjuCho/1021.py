from collections import deque
#import sys
#input = sys.stdin.readline()
#input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
poplist = list(map(int, input().split()))
# 덱큐 생성
deq = deque([i for i in range(1, N+1)])

count = 0
for pop in poplist:
    # 큐에서 뽑히기 전까지 반복
    while pop in deq:
        # 1번 연산
        if deq[0] == pop:
            deq.popleft()
        # 2번 연산
        elif deq.index(pop) <= len(deq)/2:
            deq.append(deq.popleft())
            count += 1
        # 3번 연산
        else:
            deq.appendleft(deq.pop())
            count += 1
        
print(count)
