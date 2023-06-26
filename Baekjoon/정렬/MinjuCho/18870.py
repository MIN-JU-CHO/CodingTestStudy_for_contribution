# 입력 받기
N = int(input())
X = list(map(int, input().split()))
# 원소 중복 없이 정렬
sort = sorted(set(X))
# key - 좌표값, value - sorted index
dic = { sort[i]:i for i in range(len(sort)) }
# 사전은 O(1)
for i in X:
    print(dic[i], end=' ')



# # 시간 초과 코드
# import heapq
# # 입력 받기
# N = int(input())
# X = list(map(int, input().split()))

# # 입력받은 원소 중복이 아니면 heap에 넣어 정렬
# heap = []
# for element in X:
#     if element not in heap:
#         heapq.heappush(heap, element)
# for element in X:
#     print(heap.index(element), end = ' ')
