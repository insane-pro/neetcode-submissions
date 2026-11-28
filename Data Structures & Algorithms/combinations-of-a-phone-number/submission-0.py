class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hashm={'2':'abc','3':'def','4':'ghi',
                '5':'jkl','6':'mno','7':'pqrs',
            '8':'tuv','9':'wxyz'
        }
        ret=[]
        path=[]
        def bt(st):
            if len(path)==len(digits):
                ret.append(''.join(path))
                return
            for ch in hashm[digits[st]]:
                path.append(ch)
                bt(st+1)
                path.pop()
        bt(0)
        return ret