# 3등분하고 가운데 빈칸으로 대체
def slice_line(line):
  if len(line) == 1:
    return line
  else:
    idx = len(line) // 3  # 3
    mid = [' '] * idx  # 공백으로 바꾸기
    front = slice_line(line[:idx])
    back = slice_line(line[idx * 2:])
    return front + mid + back


result = []
while True:
  try:
    n = int(input())
    line = ['-'] * (3**n)
    print(''.join(slice_line(line)))
  except:
    break
