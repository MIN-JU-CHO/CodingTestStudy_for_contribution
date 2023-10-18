# 풀이 시간: 15m
# 사용한 알고리즘: 해시와 맵 (딕셔너리)

import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
ques = list(map(int, input().split()))

cards_set = defaultdict(int)
for i in cards:
    cards_set[i] += 1

for i in ques:
    print(cards_set[i], end=" ")