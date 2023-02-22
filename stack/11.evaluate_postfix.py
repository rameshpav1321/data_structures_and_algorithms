def evaluate_postfix(expression):
    stack=[]
    for char in expression:
        if char.isdigit():
            stack.append(char)
        else:
            if stack[-1] and stack[-2]:
                val1=stack.pop()
                val2=stack.pop()
                stack.append(str(eval(val2+char+val1)))
    return stack[-1]

print(evaluate_postfix("231*+9-"))