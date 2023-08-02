# 0 ~ depth - 1 까지 좌우, 대각선 확인
def check(depth):
    for i in range(depth):
        if queen[i]==queen[depth] or (depth - i)==abs(queen[i] - queen[depth]):
            return False
    return True

def nqueen(depth):
    global result
    # 한 가지 경우 만족 시
    if depth == N:
        result += 1
        return
    # 1열씩 배치해보기
    for i in range(N):
        # 이미 방문한 것은 skip
        if visited[i] == False:
            queen[depth] = i
            if check(depth) == True:
                visited[i] = True
                # dfs
                nqueen(depth+1)
                # 다음 경우의 수를 구하기 위해 다시 false
                visited[i] = False

N = int(input())

visited = [False] * N
queen = [0] * N
result = 0

nqueen(0)
print(result)
