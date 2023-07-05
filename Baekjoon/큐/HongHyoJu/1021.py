from collections import deque

N, M = map(int, input().split())
find_arr = list(map(int, input().split()))

q = deque([i for i in range(1, N+1)])
cnt = 0

# deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).
for i in find_arr:
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            # 큐의 길이가 계속 바뀌고 있으므로 N 으로 명시하면 안되고 len(q) 으로 넣어줘야함.
            if q.index(i) <= len(q) // 2:
                while q[0] != i:
                    q.rotate(-1)
                    cnt += 1
            else:
                while q[0] != i:
                    q.rotate(1)
                    cnt += 1

print(cnt)
