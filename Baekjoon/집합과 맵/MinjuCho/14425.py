import sys
input = sys.stdin.readline
N, M = map(int, input().split())

d = {}
for _ in range(N):
    keyword = input()
    d[keyword]=True

count = 0
for _ in range(M):
    search = input()
    if search in d:
        count+=1
print(count)
