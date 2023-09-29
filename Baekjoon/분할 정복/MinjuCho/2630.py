# 문제 풀이 링크: https://velog.io/@cuppizza/백준-2630-색종이-만들기-파이썬-C
import sys
input = sys.stdin.readline
N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
counts = [0, 0]

def div_half(x, y, n):
    half = int(n/2)
    if n == 1:
        counts[paper[y][x]]+=1
        return
    else:
        pivot = paper[y][x]
        isPivot = True
        for i in range(y, y+n):
            for j in range(x, x+n):
                if paper[i][j] != pivot:
                    isPivot = False
                    break
            if isPivot == False:
                break
        if isPivot == False:
            div_half(x, y, half)
            div_half(x+half, y, half)
            div_half(x, y+half, half)
            div_half(x+half, y+half, half)
        else:
            counts[paper[y][x]]+=1
            return

div_half(0,0,N)
print(counts[0])
print(counts[1])
