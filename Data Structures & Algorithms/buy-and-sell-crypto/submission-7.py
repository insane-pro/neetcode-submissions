class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        l=0
        r=1
        while (l<r )and(r<len(prices)) :
            if prices[l]<prices[r]:
                maxi=max(maxi,prices[r]-prices[l])
            else:
                l=r
            r+=1
        return maxi

        