'''
Topic: Array (Two Pointers)
Difficulty: Easy

Say you have an array for which the ith element is the price of a given stock on the ith day.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
Example:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Not 7-1 = 6, as selling price needs to be larger than buying price.

Time Complexity: O(n), where n is the number of days (length of the prices array).
Space Complexity: O(1), as we are using only a few extra variables.
'''

def maxProfit(prices):
    if not prices:
        return 0
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


def maxProfit_v2(prices):
    if not prices:
        return 0
    left_pointer, right_pointer = 0, 1
    max_profit = 0
    while right_pointer < len(prices):
        if prices[right_pointer] > prices[left_pointer]:
            profit = prices[right_pointer] - prices[left_pointer]
            max_profit = max(max_profit, profit)
        else:
            left_pointer = right_pointer
        right_pointer += 1
    return max_profit