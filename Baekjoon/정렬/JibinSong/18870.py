# # 시간 초과

# n = int(input())
# arr = list(map(int, input().split()))

# a = sorted(set(arr))
# print(*list(map(a.index, arr)))

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(set(arr))
dic_arr = dict(zip(arr2, range(len(arr2))))
for i in arr:
  print(dic_arr[i], end=' ')
