# "." 입력 전까지 입력받기
while True:
    sentence = input()
    stack = []
    if sentence == ".":
        break
    # 한 문장 전체 괄호 추출 및 스택에 넣기
    for char in sentence:
        # 여는 괄호는 스택에 넣기
        if char == '[' or char == '(':
            stack.append(char)
        # 닫는 괄호는 이전 짝과 반드시 매칭 돼야만 팝되고 넘어간다.
        elif char == ']':
            if len(stack)!=0 and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(char)
                break;
        elif char == ')':
            if len(stack)!=0 and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(char)
                break;
    if len(stack)==0:
        print("yes")
    # 닫는 괄호가 하나라도 매칭 되지 않을 때
    else:
        print("no")
        
