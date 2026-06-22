class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        par={'}':"{",")":"(",']':"["}
        for c in s:
            if stack and ( c in par and stack[-1]==par[c]):
                stack.pop()
            else:
                stack.append(c)

        return not stack
        

