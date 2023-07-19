def merge_sort(array, p, r):
  print('first', p, r)
  if r-p >= 2:
    q = (p + r) // 2
    # 전반부 정렬
    merge_sort(array, p, q)
    # 후반부 정렬
    merge_sort(array, q + 1, r)
    # 병합
    merge(array, p, q, r)


def merge(array, p, q, r):
  global cnt
  i = p
  j = q + 1
  temp = []
  while i <= q and j <= r:
    if array[i] <= array[j]:
      temp.append(array[i])
      print("temp", temp)
      i += 1
    else:
      temp.append(array[j])
      # print("temp", temp)
      j += 1
  # 왼쪽 배열이 남은 경우
  while i <= q:
    temp.extend(array[i:])
    # print("temp", temp)
  # 오른쪽 배열이 남은 경우
  while j <= r:
    temp.extend(array[j:])
    # print("temp", temp)

  array[p:r] = temp
  result.append(temp)  # 저장된 원소 리스트


n, m = map(int, input().split())
array = list(map(int, input().split()))
result = []
merge_sort(array, p=0, r=len(array) - 1)
print(result)
