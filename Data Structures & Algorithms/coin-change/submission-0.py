class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [amount+1] * (amount+1)
        memo[0] = 0

        for a in range(1, amount +1) :
            for c in coins:
                if a-c >= 0:
                    memo[a] = min(memo[a], 1 + memo[a-c])
        if memo[amount] > amount:
            return -1
        return memo[amount]
                 # first check if 1 can be satisfied
                 # for 2 check if curr amount - curr coin is better than curr memo
