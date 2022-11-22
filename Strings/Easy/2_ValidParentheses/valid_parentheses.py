from collections import deque

mappings = {
    '}' : '{',
    ')' : '(',
    ']' : '['
}

# If opening bracket, push to stack
# else : If closing bracket, check if the corresponding opening bracket is in the top of the stack
def isValid(s: str) -> bool:
    stack = deque()
    
    for p in s:
        # 1) Always push opening bracket into stack
        if p not in mappings:
            stack.appendleft(p)
        # 2) If closing bracket
        else:
            # If stack not empty, pop the top element to compare
            # else : replace it with '#'
            topEle = stack.popleft() if stack else '#'
            if topEle != mappings[p]:
                return False
    
    return not stack

if __name__ == "__main__":
    s1 = "(])"
    print(f"Are the parentheses in {s1} valid ? {isValid(s1)}")
    s2 = "()[]{}"
    print(f"Are the parentheses in {s2} valid ? {isValid(s2)}")