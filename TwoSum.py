#O(n) time
#Use a hash table to store the numbers as keys and the indices as values.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Initialize empty dictionary
        #to store the value and the index of each list element as a key-pair.
        mp = {}
        
        #Iterate through the indices and values of the list containing our numbers.
        #Check to see if the difference (target - number) is in the hash table.
        for i, num in enumerate(nums):
            difference = target - num
            if difference in mp:
                return [mp[difference],i]
            else:
                mp[num]=i
                

#O(n^2) time
#Use two for loops to loop through the array and find the indices
#of the two numbers that add up to the target number.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return[i,j]
        
