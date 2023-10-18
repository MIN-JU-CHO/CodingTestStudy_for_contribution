import sys
input = sys.stdin.readline

N, C = map(int, input().split())
array = []
for _ in range(N):
    array.append(int(input()))
array.sort()

def bin_search(start, end):
    if start > end:
        return
    # 거리 맞혀보기
    mid = (start + end)//2
    # 가장 왼쪽 집부터 설치
    last = 0
    count = 1
    for i in range(len(array)):
        #공유기 설치
        if array[i] - array[last] >= mid:
            last = i
            count +=1
    # 거리 값 더 늘려도 될 때
    if count >= C:
        global result
        result = mid
        bin_search(mid+1, end)
    # 설치하기에 부족하여 거리 값 더 좁혀야할 때
    else:
        bin_search(start, mid-1)

bin_search(1, array[-1] - array[0])
print(result)
