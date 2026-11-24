class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
       
        ret=[]
        sol=[]
        def bt(s):
            ret.append(sol[:])
               
            for i in range(s,n):
                
                if i>s and nums[i]==nums[i-1] :continue
                
                sol.append(nums[i])
                bt(i+1)
                sol.pop()
                
        bt(0)
        return ret 
        