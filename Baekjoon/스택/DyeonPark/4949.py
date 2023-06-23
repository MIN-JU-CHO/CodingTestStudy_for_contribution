import re
import sys
input = sys.stdin.readline

def isListEmpty(brackets: list):
  if len(brackets) == 0:
    return True
  else:
    return False

while True:
  sen = input().rstrip()
  if sen == ".":
    break
  else:
    sen = re.sub("[^\[\]()]", "", sen)

  brackets = []
  iswrongstart = False
  for i in sen:
    if i in ["[", "("]:
      brackets.append(i)
    elif i in ["]", ")"]:
      if isListEmpty(brackets):
        iswrongstart = True
        break
      top = brackets[-1]
      answer = "[" if i == "]" else "("
      if top != answer:
        break
      else:
        brackets.pop()

  if len(brackets) > 0 or iswrongstart:
    print("no")
  else:
    print("yes")
