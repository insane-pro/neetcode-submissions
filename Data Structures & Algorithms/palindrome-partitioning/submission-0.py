class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret,path=[],[]
        def bt(st):
            if st==len(s):
                ret.append(path[:])
                return
            for end in range(st,len(s)):
                sub=s[st:end+1]
                if sub[::-1]==sub:
                    path.append(sub)
                    bt(end+1)
                    path.pop()
        bt(0)    
        return ret

        