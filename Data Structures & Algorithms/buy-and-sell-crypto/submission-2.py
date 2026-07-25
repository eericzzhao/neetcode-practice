class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left = buy, right = sell
        maxProfit = 0

        while r < len(prices):
            # it is profitable: new price > old price
            if prices[r] > prices[l]:
                # calculate the new profit and compare
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                # not profitable -> we can just move our l -> r
                l = r
            r += 1
        return maxProfit
        