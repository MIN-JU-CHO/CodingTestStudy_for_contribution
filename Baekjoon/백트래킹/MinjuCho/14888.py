from itertools import permutations
import sys
import math
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
num_opers = list(map(int, input().split()))

# 각 수만큼 oper 담기
operators = []
for i in range(4):
    if i==0:
        operators.extend('+' * num_opers[i])
    elif i==1:
        operators.extend('-' * num_opers[i])
    elif i==2:
        operators.extend('*' * num_opers[i])
    elif i==3:
        operators.extend('/' * num_opers[i])
# 모든 순열 경우 구하기
combs_opers = list(permutations(operators, N-1))

# 모든 경우 값 구해, 최소 최대 구하기
maximum = 0
minimum = int(1e9)
for opers in combs_opers:
    temp = nums[0]
    #print(temp, end = ' ')
    for i in range(1, N):
        if opers[i-1] == '+':
            temp += nums[i]
            #print('+', nums[i], end = ' ')
        elif opers[i-1] == '-':
            temp -= nums[i]
            #print('-', nums[i], end = ' ')
        elif opers[i-1] == '*':
            temp *= nums[i]
            #print('*', nums[i], end = ' ')
        elif opers[i-1] == '/':
            if temp < 0:
                temp = (-temp) // nums[i]
            else:
                temp = temp // nums[i]
            #print('/', nums[i], end = ' ')
    #print(' =', temp)
    if temp > maximum:
        maximum = temp
    if temp < minimum:
        minimum = temp
print(maximum)
print(minimum)
