class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Initilaize max_profit variable
        max_profit = 0
        #Initilaize  min_price variable and set it to first value in the array
        minimum_num = prices[0]
        
        #Iterate through the array
        #Check if next value in array are less than the the first value in the array
        #if true set min_price to the lesser value
        for i in prices:
            if i < minimum_num:
                minimum_num = i
            #max() function returns the item with the highest value, 
            #or the item with the highest value in an iterable.
            #Return 0 if array is empty (max_profit = 0)
            #OR
            #Return max_profit
            max_profit = max(max_profit, i - minimum_num)
        return max_profit
