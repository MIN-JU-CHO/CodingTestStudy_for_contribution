n = int(input())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[0])

arr2 = [i[1] for i in arr]

# 가장 긴 증가하는 부분 수열을 구한다.
# ex) [8, 2, 9, 1, 4, 6, 7, 10]
dp = [1] * n

def count_ascending(key_idx):
  if (key_idx+1) == n:
    return
  else:      
    for i in range(key_idx+1, n):
      if arr2[key_idx] < arr2[i]:
        dp[key_idx] = max(dp[key_idx], dp[i]+1)
        
for i in range(n-1, -1, -1):
  count_ascending(i)

print(n-max(dp))

      
