# 대칭 차집합
N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(set(A-B).union(set(B-A))))
