def infix_to_prefix(expression):
    stack=[]
    output=''
    precedence={'+':1,'-':1,'*':2,'/':2,'^':3}
    for i in range(len(expression)):
        curr=expression[~i]
        if curr.isalpha():
            output+=curr
        elif curr==')':
            stack.append(curr)
        elif curr in '+-*/^':
            while stack and stack[-1]!=')' and precedence[stack[-1]]>=precedence[curr]:
                output+=stack.pop()
            stack.append(curr)
        elif curr=='(':
            while stack and stack[-1]!=')':
                output+=stack.pop()
            stack.pop()
    while stack:
        output+=stack.pop()
    return ''.join(list(reversed(output)))

print(infix_to_prefix("(A-B/C)*(A/K-L)"))
