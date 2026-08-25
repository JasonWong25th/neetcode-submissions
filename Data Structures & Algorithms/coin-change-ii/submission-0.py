class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #we can calcuate bottom uo
        #at every amount we can calcuate
        #how many coins combinations can make that amount

        combinations = [0] * (amount +1)
        combinations[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                combinations[i] += combinations[i -coin]
        return combinations[amount]