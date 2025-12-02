class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=10**18
        best=0
        for p in prices:
            if p<minPrice:
                minPrice=p
            else :
                best=max(best,p-minPrice)
        return best
        