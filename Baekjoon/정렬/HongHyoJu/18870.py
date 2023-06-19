# list.index(i) 형태의 시간 복잡도 = O(N)
# { dict[요소] : 요소의 index } 형태의 시간 복잡도 = O(1)

N = int(input())
arr = list(map(int, input().split()))
newArr = sorted(set(arr))

dic = {}
for i in range(len(newArr)):
    dic[newArr[i]] = i

for i in arr:
    print(dic[i], end=' ')
