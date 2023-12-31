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
  # 간격을 1칸보다 더 뛰어 넘을 수 있으므로 이전 값도 비교대상에 추가가 된다.
  dp[2] = max(dp[0]+arr[2], arr[1]+arr[2], dp[1])
if n >= 4:
  # 3은 dp[3] = max(dp[1]+arr[3], dp[0]+arr[2]+arr[3])
  for i in range(3, n):
    dp[i] = max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i], dp[i-1])

# print(dp[-1])
print(max(dp))

