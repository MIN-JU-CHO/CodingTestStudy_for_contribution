while True:
  s = input()
  arr = []
  f = True
  if s == '.':
    break
  else:
    for i in s:
      # print(arr)
      if i == "(" or i == "[":
        arr.append(i)
      if i == ')':
        if arr and arr.pop() == '(':
          pass
        else:
          f = False
          break
      if i == ']':
        if arr and arr.pop() == '[':
          pass
        else:
          f = False
          break
    if (not arr) and f:
      print('yes')
    else:
      print('no')
