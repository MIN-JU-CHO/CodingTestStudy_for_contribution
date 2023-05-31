N = int(input())
scores = list(map(int, input().split()))
M = max(scores)
accum=0
for i in range(0,N):
    scores[i] = scores[i]/M*100
    accum+=scores[i]
print(accum/N)
