class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dec={}
        freq=[]
        for i in range(len(nums)):
            dec[nums[i]]=dec.get(nums[i],0)+1

        res=[]

        for n,c in dec.items():
            freq.append([c,n])
            freq.sort()

        while len(res)<k:
            res.append(freq.pop()[1])
        return res
