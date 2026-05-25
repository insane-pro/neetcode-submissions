class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret={}
        for i,j in enumerate(nums):
            diff =target-j
            if diff  in ret:
                return[ret[diff],i]

            ret[j]=i
