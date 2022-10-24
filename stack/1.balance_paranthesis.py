def matching(char1,char2):
    if char1=='(' and char2==')' or char1=='[' and char2==']'or char1=='{' and char2=='}':
        return True
    else:
        return False
    
def balance_paranthesis(str):
    stack=[]
    for char in str:
        if char=='(' or '[' or '{':
            stack.append(char)
        else:
            if len(stack)==0:
                return False
            if not matching(stack[-1],char):
                return False
            else:
                stack.pop()
    return len(stack)==0
