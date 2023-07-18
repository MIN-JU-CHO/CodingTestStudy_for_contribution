def contour(N, start, end):
  if N == 1:
    return 
  else:
    term = N // 3

    contour(term, start, term)
    res[start + term:start + term + term] = [' '] * term
    contour(term, start + term + term, end)

while True:
  try:
    N = 3**int(input())
    res = ['-'] * (N)
  
    contour(N, 0, N)
    print(''.join(res))
  except:
    break
