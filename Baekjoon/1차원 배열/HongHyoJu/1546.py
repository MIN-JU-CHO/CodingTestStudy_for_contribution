N = int(input())
scores = list(map(int, input().split()))
M = max(scores)

new_list = []
for score in scores :
    new_list.append(score/M *100)
new_avg = sum(new_list)/N
print(new_avg)