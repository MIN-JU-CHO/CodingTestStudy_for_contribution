from itertools import permutations
import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
num_opers = list(map(int, input().split()))

maximum = int(-1e9)
minimum = int(1e9)

def operate(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    # 하나의 경우의 수 연산 끝마침
    if depth == N:
        if total > maximum:
            maximum = total
        if total < minimum:
            minimum = total
        return
    # 연산자 수 1 이상일 때 다 해보기
    if plus:
        operate(depth+1, total+nums[depth], plus-1, minus, multiply, divide)
    if minus:
        operate(depth+1, total-nums[depth], plus, minus-1, multiply, divide)
    if multiply:
        operate(depth+1, total*nums[depth], plus, minus, multiply-1, divide)
    if divide:
        operate(depth+1, int(total/nums[depth]), plus, minus, multiply, divide-1)

operate(1, nums[0], num_opers[0], num_opers[1], num_opers[2], num_opers[3])

print(maximum)
print(minimum)
