white = [[0]*100 for _ in range(100)]
num = int(input())
for i in range(0,num):
    wid, hei = map(int, input().split())
    for width in range(wid-1, wid+9):
        for height in range(hei-1, hei+9):
            white[width][height] = 1
count = 0
for i in range(100):
    for j in range(100):
        if white[i][j]==1:
            count+=1    
print(count)
