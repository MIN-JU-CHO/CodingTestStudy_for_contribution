import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = max(nums)

after = [i/M*100 for i in nums]
print(sum(after)/N)