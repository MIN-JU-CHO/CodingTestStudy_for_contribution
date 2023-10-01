# dp, 이진 탐색 이용 알고리즘 - dp만 사용
# 실행 시간: 132ms, 사용 메모리: 4.2 MB
from bisect import bisect_left
import sys
input = sys.stdin.readline
while True:
    try:
        N = int(input())
        dp=[]
        for stock in map(int, input().split()):
            index = bisect_left(dp, stock)
            if index == len(dp):
                dp.append(stock)
            else:
                dp[index] = stock
        print(len(dp))
    except:
        break



# dp, 이진 탐색 이용 알고리즘 - NlogN 정석
# 실행 시간: 128ms, 사용 메모리: 4.4 MB
from bisect import bisect_left
import sys
input = sys.stdin.readline
while True:
    try:
        N = int(input())
        stock = list(map(int, input().split()))
        dp = [1]
        arr = [stock[0]]
        for i in range(1, N):
            index = bisect_left(arr, stock[i])
            if index == len(dp):
                arr.append(stock[i])
                dp.append(dp[-1]+1)
            else:
                arr[index] = stock[i]
        print(dp[-1])
    except:
        break
