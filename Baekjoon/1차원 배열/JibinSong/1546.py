n = int(input())
scores = list(map(int, input().split()))

M = max(scores)

new_scores = list(map(lambda x: x/ M * 100,scores))
print(sum(new_scores)/n)
