class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret=[]
        path=[]
        def bt(o,c):
            if o==c==n:
                ret.append(''.join(path))
                return 
            if o<n:
                path.append('(')
                bt(o+1,c)
                path.pop()
                
            if c<o:
                path.append(')')
                bt(o,c+1)
                path.pop()
        bt(0,0)
        return ret
        