import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

comp_info = sorted(list(set(nums))) # O(N) + O(NlogN)

comp = defaultdict(int)
for idx, val in enumerate(comp_info): # O(N')
  comp[val] = idx

ans = [comp[i] for i in nums] # O(N)
print(*ans)
