### version1 ###

# 주어진 값 입력 받기
n = int(input())
squares = []
for i in range(n):
  x, y = map(int,input().split())
  squares.append((x,y))

# 도화지 초기화
arr = [[0 for i in range(100)] for j in range(100)]

for square in squares:
  x = square[0]
  y = square[1]

  for i in range(x,x+10):
    for j in range(y,y+10):
      arr[i][j] = 1

result = 0
for i in arr:
  result += sum(i)
print(result)

### version 2 ###

# 주어진 값 입력 받기
n = int(input())
squares = []
for i in range(n):
  x, y = map(int,input().split())
  squares.append((x,y))

# 도화지 초기화
arr = [[0 for i in range(100)] for j in range(100)]

for square in squares:
  x = square[0]
  y = square[1]

  for i in range(x,x+10):
    for j in range(y,y+10):
      arr[i][j] = 1

result = 0
for i in arr:
  for j in i:
    if j:
      result += 1
print(result)

