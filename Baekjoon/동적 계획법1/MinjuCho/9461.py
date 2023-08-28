# https://velog.io/@cuppizza/백준-9461-파도반-수열-파이썬
import sys
input = sys.stdin.readline

P = [0] * 100
P[0] = 1
P[1] = 1
P[2] = 1

def recurrence(index):
    global P
    if P[index] != 0:
        return
    P[index] = P[index-3]+P[index-2]

T = int(input())
for _ in range(T):
    N = int(input())
    for i in range(3, N):
        recurrence(i)
    print(P[N-1])
