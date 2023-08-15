import sys
input = sys.stdin.readline
minimum = int(1e9)

def dfs(depth, N, visited, S, idx):
    global minimum
    if depth == N/2+1:
        count=0
        link = 0
        start = 0
        #print(visited, end = " ")
        for i in range(len(visited)):
            for j in range(len(visited)):
                if visited[i]==0 and visited[j] == 0:
                    link+=S[i][j]
                    continue
                elif visited[i]==1 and visited[j] == 1:
                    start+=S[i][j]
                    continue
        count = abs(link-start)
        #print(count)
        minimum = min(count, minimum)
    else:
        for i in range(idx, len(visited)):
            visited[i] = 1
            dfs(depth+1, N, visited, S, i+1)
            visited[i] = 0

N = int(input())
visited = [0] * N
S = []
for i in range(N):
    S.append(list(map(int, input().split())))
dfs(1, N, visited, S, 0)
print(minimum)
