https://ji-gwang.tistory.com/260

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * (N + 1)
result = int(1e9)


def solve(depth, idx):
    global result
    if depth == (N // 2):
        start, link = 0, 0
        for i in range(N):
            for j in range(i + 1, N):
                if visited[i] and visited[j]:
                    start += S[i][j] + S[j][i]
                elif not visited[i] and not visited[j]:
                    link += S[i][j] + S[j][i]
        result = min(result, abs(start - link))

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            solve(depth + 1, i + 1)
            visited[i] = False


solve(0, 0)
print(result)
