import sys
input = sys.stdin.readline
N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
counts = [0, 0, 0]

def div_half(x, y, n):
    half = int(n/3)
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
            div_half(x+2*half, y, half)
            div_half(x, y+half, half)
            div_half(x+half, y+half, half)
            div_half(x+2*half, y+half, half)
            div_half(x, y+2*half, half)
            div_half(x+half, y+2*half, half)
            div_half(x+2*half, y+2*half, half)
        else:
            counts[paper[y][x]]+=1
            return

div_half(0,0,N)
print(counts[-1])
print(counts[0])
print(counts[1])
