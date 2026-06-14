class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret=[]
        temp=sorted(nums)
        for i,j in enumerate(temp):
            if (i>0) and (j == temp[i-1]):
                continue

            l=i+1
            r=len(temp)-1
            while l<r:
                cs=j+temp[l]+temp[r]

                if cs>0:
                    r-=1

                elif cs<0:
                    l+=1

                else:
                    ret.append([j,temp[l],temp[r]])
                    l+=1

                    while (l<r) and (temp[l]==temp[l-1]):
                        l+=1
    
        return ret