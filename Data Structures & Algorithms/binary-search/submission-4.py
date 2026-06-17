class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ret=-1
        n=len(nums)
        l=0
        r=n-1
        while l<=r:
            m=l+((r-l)//2)
            if nums[m]==target:
                ret=m
                break
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
        return ret