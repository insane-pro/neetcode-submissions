class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ret=[]
        ans=[0]*n
        for i in range(n):
            while ret and temperatures[ret[-1]]<temperatures[i]:
                prev=ret.pop()
                ans[prev]=i-prev
            ret.append(i)
            
            
        return ans


        