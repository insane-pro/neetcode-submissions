class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret=[]
        nums.sort()
        for i,j in enumerate(nums):
            if (i>0) and (j == nums[i-1]):
                continue

            l=i+1
            r=len(nums)-1
            while l<r:
                cs=j+nums[l]+nums[r]

                if cs>0:
                    r-=1

                elif cs<0:
                    l+=1

                else:
                    ret.append([j,nums[l],nums[r]])
                    l+=1

                    while (l<r) and (nums[l]==nums[l-1]):
                        l+=1
    
        return ret