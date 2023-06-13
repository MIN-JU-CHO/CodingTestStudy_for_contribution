from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = []

for i in list(combinations(cards, 3)):
  if sum(i) <= M:
    result.append(i)

print(sum(max(result, key = lambda x : sum(x))))
