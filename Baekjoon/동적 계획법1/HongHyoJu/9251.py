a = input()
b = input()

dp = [[0] * (len(a)+1) for _ in range(len(b)+1)]

for row in range(1, len(a) + 1):
    for col in range(1, len(b) + 1):
        if a[row - 1] == b[col - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

print(dp[-1][-1])
