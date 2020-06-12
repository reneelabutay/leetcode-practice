"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = []
        found = False
        
        for num in range(len(nums)):
            current = nums[num] 
            if (found == False):
                for i in range(num+1, len(nums)):
                    if(current + nums[i] == target):
                        indices.append(num)
                        indices.append(i)
                        found = True
                        break
        
        return indices