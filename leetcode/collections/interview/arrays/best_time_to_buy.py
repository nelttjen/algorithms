from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought_price = prices[0]

        profit = 0

        for i in range(1, len(prices) - 1):
            this_val = prices[i]
            if this_val > bought_price and this_val > (val := prices[i + 1]):
                profit += this_val - bought_price
                bought_price = val
            elif this_val < bought_price:
                bought_price = this_val
        if (val := prices[-1]) > bought_price:
            profit += val - bought_price
        return profit


if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))