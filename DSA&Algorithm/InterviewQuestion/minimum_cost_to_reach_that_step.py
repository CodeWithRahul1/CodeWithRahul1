'''Given N steps having positive integers which signifies the cost of the moving from each step. Paying the cost at i-th step, you can either climb

one or two steps. Given that one can start from the 0-the step or 1-the step.

the task is to find the minimum cost to reach the top of the floor(N+1) by climbing

N(maximum) step.

Examples:

Input: a[] = {15, 21, 11, 10, 18)

Output: 31

Start from 21 and then move to 10.

Input: a[] = (2. 7. 4. 2. 7, 5. 9)

Output: 13

2->4->2->5'''

def minCostClimbingStairs(cost):
    n = len(cost)
    dp = [0] * (n + 1)  
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1],  
                    dp[i - 2] + cost[i - 2])  
    
    return dp[n]

# Example usage:
arr1 = [15, 21, 11, 10, 18]
print(minCostClimbingStairs(arr1))  # Output: 31

arr2 = [2, 7, 4, 2, 7, 5, 9]
print(minCostClimbingStairs(arr2))  # Output: 13
