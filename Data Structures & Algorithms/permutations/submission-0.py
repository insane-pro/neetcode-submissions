class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret=[]
        use=[False]*len(nums)
        def bt(sol):
            if len(sol)==len(nums):
                ret.append(sol[:])
                return 
            for i in range(len(nums)):
                if use[i]:  
                    continue
                if i>0 and nums[i]==nums[i-1] and not use[i-1]:continue
                use[i] = True
                sol.append(nums[i])
                bt(sol)
                sol.pop()
                use[i] = False
        bt([])
        return ret
