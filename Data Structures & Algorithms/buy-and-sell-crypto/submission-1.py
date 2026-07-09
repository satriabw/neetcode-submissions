class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two iteration is easy just find max and then iterate most profit after max:
        # or just buy at i, check if next is increase just sell

        max_profit = 0
        current = prices[0]
        for i in range(1, len(prices)):
            # If next is less than today sell without profit, move current
            if current >= prices[i]:
                current = prices[i]
            # If it is bigger update max profit
            else:
                max_profit = max(max_profit, prices[i]-current)
        
        return max_profit