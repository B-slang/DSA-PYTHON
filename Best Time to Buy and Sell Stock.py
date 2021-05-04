class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        d_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices) ):
            profit = prices[i]-d_price
            
            if profit > max_profit:
                max_profit = profit
    
            if d_price > prices[i]:
                    d_price = prices[i]
        return max_profit
        