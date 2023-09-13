import sys
input = sys.stdin.readline
B = [501] * 501
dp = [1] * 501

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    B[a] = b

for a in range(1, 501):
    for j in range(1, a):
        if B[j] < B[a] and B[a] != 501:
            # 안겹치는 경우 찾기
            dp[a] = max(dp[j]+1, dp[a])

print(N - max(dp))

#-------------------------------
## 틀린 풀이
#import sys
#input = sys.stdin.readline
#N = int(input())
#A = [i for i in range(501)]
#B = [501]*501
#dp = [1]*501

## 전깃줄 정보 입력
#for i in range(N):
#    a, b = map(int, input().split())
#    B[a] = b

## 큰 값이 있는데 초기값이 아닐 때 겹치는 줄의 dp값
#for a in range(1, 501):
#    for j in range(1, a): 
#        if B[a] < B[j] and B[j] != 501:
#            dp[a] = max(dp[j]+1, dp[a])

#print(max(dp))

#--------------------------------
## 틀린 풀이
#import sys
#input = sys.stdin.readline
#N = int(input())
#A = [i for i in range(501)]
#B = [501]*501

## 전깃줄 정보 입력
#for i in range(N):
#    a, b = map(int, input().split())
#    B[a] = b
    
## 큰 값이 있는데 초기값이 아닐 때 겹치는 줄의 index 저장
#prob = []
#for a in range(1, 501):
#    for j in range(1, a):
#        #print("a: ", a, "j:", j)
#        if B[a] < B[j] and B[j] != 501:
#            #print("B[",a,"]:", B[a], "B[",j,"]:", B[j])
#            prob.append(j)
#result = list(set(prob))
##print(result)

#print(len(result))
