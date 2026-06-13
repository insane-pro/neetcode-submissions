class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num=set(nums)
        longest=0
        for n in set_num:
            if (n-1) not in set_num:
                length=0
                while(n+length) in set_num:
                    length+=1
                    longest=max(longest,length)
        return longest   

            


        