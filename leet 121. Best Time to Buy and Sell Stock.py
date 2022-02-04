class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit 과 min_price에는 각각 최솟값, 최댓값을 지정해놓는다 그래야 아래 for 구문에서 TypeError가 발생하지 않는다.
        profit = 0
        min_price = sys.maxsize
        
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
            
        return profit
