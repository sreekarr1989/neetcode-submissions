class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 #buy day
        r = 1 #sell day
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit,profit)
            else:
                #we found our new low price
                l = r
            r +=1
        return maxProfit


        '''result = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                sell = prices[j]
                result = max(result, sell - buy)
        
        return result'''
