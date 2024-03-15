import timeit
import collections
def min_coins(coins, target):
    # Initialize array to store minimum coins for each value from 0 to target
    dp = [[0] * (target + 1) for _ in range(len(coins) + 1)]
    #dp[0] = 0  # Base case: 0 coins needed to make 0

    # Initialize a dictionary to store the count of each coin denomination
    # coin_counts = {coin: 0 for coin in coins}

    # Iterate over each coin denomination
    for i in range(0, len(coins)):
        # Update dp array for each value from coin to target
        for j in range(0, target + 1):
            if (coins[i] == 0) or (j == 0):
                dp[i][j] = []
                continue
            if j < coins[i]:
                dp[i][j] = dp[i - 1][j]
                continue
            elif j == coins[i]:
                dp[i][j] = [coins[i]]
                continue
            else:
                dp[i][j] = dp[i][j - coins[i]] + [coins[i]]

    # Construct result dictionary with only the required coin denominations
    result = dp[len(coins) - 1][target]

    return collections.Counter(result)

# Example usage
coins = [1, 2, 5, 10, 25]
target = 1113
result = min_coins(coins, target)
print("Amount of each coin needed to achieve the target sum:")
print(result)

execution_time = timeit.timeit(lambda: min_coins(coins, target), number = 1)

print("Execution time:", execution_time, 'seconds') 

            



