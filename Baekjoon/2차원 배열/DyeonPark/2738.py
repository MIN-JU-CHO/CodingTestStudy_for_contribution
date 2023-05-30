N, M = map(int, input().split())
mat_A = [list(map(int, input().split())) for _ in range(N)]
mat_B = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
  for j in range(M):
    print(mat_A[i][j] + mat_B[i][j], end=' ')
  print()
