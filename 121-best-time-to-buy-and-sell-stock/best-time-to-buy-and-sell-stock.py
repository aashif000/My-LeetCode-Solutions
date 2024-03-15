class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        if len(prices)==1:
            return 0
        i,j = 0,1
        n = len(prices)
        while j<n:
            if prices[i]>prices[j]:
                i = j
            else:
                res = max(res, prices[j]-prices[i])
            j+=1
                
        return res
