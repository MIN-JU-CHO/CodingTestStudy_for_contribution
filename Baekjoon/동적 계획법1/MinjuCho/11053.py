import sys
input = sys.stdin.readline

def binary_search(table, left, right, value):
    mid = (left+right)//2
    # 못찾음
    if left > right :
        return -1
    # 찾은 자리
    if table[mid] < value <= table[mid+1]:
        return mid+1
    if value <= table[mid]:
        return binary_search(table, left, mid-1, value)
    if value > table[mid]:
        return binary_search(table, mid+1, right, value)


N = int(input())
A = list(map(int, input().split()))
table = [0] * (N+1)
dpLength = 1

for i in range(N):
    index = binary_search(table, 0, dpLength-1, A[i])
    #print("A[i] =", A[i], "index =", index)
    
    # new insert
    if index == -1:
        table[dpLength] = A[i]
        dpLength += 1

    # update table
    else:
        table[index] = A[i]
    #print(table, "dpLength = ", dpLength)
print(dpLength-1)
