class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ret,sol=[],[]
        def bt(s,rem):
            if rem==0:
                ret.append(sol[:])
                return
            for i in range(s,len(nums)):
                if i>s and nums[i]==nums[i-1]:
                    continue
                if nums[i]>rem:
                    break
                sol.append(nums[i])
                bt(i+1,rem-nums[i])
                sol.pop()
        bt(0,target)
        return ret
        