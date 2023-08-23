'''
a b c d e f g

a의 최대 = a
b의 최대 = a+b
c의 최대 = a+c | b+c
	a가 왔을 때는 a의 최대를 가져옴
	b가 왔을 때는 b와 이전이전을 고려해야되는데, 없음. 따라서 d부터 진행한다.

여기서부터 점화식 시작!
d의 최대 = a+b+d | a+c+d
	b가 왔을 때는 b까지의 최대 가져옴
	c가 왔을 때는 로컬c와 a까지의 최대를 가져옴
e의 최대 = a+b+d+e | a+c+e | b+c+e
	c가 왔을 때는 상관없음, c까지의 최대만 가져온다.
	d가 왔을 때는 이전이전인 b까지의 최대를 고려. b가 최대인 것을 가져옴
'''

n = int(input())
arr = []
for i in range(n):
  arr.append(int(input()))

# print(arr)

dp = [0]*n
if n >= 1:
  dp[0] = arr[0]
if n >= 2:
  dp[1] = dp[0] + arr[1]
if n >= 3:
  dp[2] = max(dp[0]+arr[2], arr[1]+arr[2])
if n >= 4:
  # 3은 dp[3] = max(dp[1]+arr[3], dp[0]+arr[2]+arr[3])
  for i in range(3, n):
    dp[i] = max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])

print(dp[-1])

