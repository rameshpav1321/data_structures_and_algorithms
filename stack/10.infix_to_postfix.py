def infix_to_postfix(expression):
    stack=[]
    output=""
    precedence={'+':1,'-':1,'*':2,'/':2,'^':3}
    for char in expression:
        if char.isalpha():
            output+=char
        elif char=='(':
            stack.append(char)
        elif char in '+-*/^':
            while stack and stack[-1]!='(' and precedence[stack[-1]]>=precedence[char]:
                output+=stack.pop()
            stack.append(char)
        elif char==')':
            while stack and stack[-1]!='(':
                output+=stack.pop()
            stack.pop()
    while stack:
        output+=stack.pop()
    print(output)


infix_to_postfix("a+b*(c^d-e)^(f+g*h)-i")
                


