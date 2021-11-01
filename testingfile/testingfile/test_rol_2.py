def is_balanced(s): 
    stack = [] 
    open_bracket = ['{', '[', '('] 
    close_bracket = ['}', ']', ')'] 
    for i in range(len(s)): 
        if s[i] in open_bracket: 
            stack.append(s[i]) 
        elif s[i] in close_bracket: 
            index = close_bracket.index(s[i]) 
            if len(stack) > 0 and stack[-1] == open_bracket[index]: 
                stack.pop() 
            else: 
                return False
            break 
    if len(stack) != 0: 
        return False
    else:
        return True


print(is_balanced("(555)"))
