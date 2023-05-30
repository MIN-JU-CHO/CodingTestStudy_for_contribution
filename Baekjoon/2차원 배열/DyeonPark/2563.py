# Data input
N = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(N):
  # set pos
  x, y = map(int, input().split())

  # coloring with black(1)
  for idx_x in range(10):
    for idx_y in range(10):
      paper[x+idx_x][y+idx_y] = 1

# cal result
result = 0
for i in range(100):
  result += sum(paper[i])
print(result)

# Q. How can we use mathematical algorithms?