# 문제 풀이 링크: https://velog.io/@cuppizza/백준-1992-쿼드트리-파이썬-C
import sys
input = sys.stdin.readline
N = int(input())
paper = []
for _ in range(N):
    paper.append(list(input().rstrip()))
result = []

def div_half(x, y, n):
    half = int(n/2)
    if n == 1:
        result.append(paper[y][x])
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
            result.append("(")
            div_half(x, y, half)
            div_half(x+half, y, half)
            div_half(x, y+half, half)
            div_half(x+half, y+half, half)
            result.append(")")
        else:
            result.append(paper[y][x])
            return

div_half(0,0,N)
result = ''.join(result)
print(result)
