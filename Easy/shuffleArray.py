'''
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

'''

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        
        newArr = [] #return this
        
        firstHalf = nums[:n]
        secondHalf = nums[n:]
        
        assert(len(firstHalf) == len(secondHalf))
        #iterate through and append
        for i in range(n):
            newArr.append(firstHalf[i])
            newArr.append(secondHalf[i])
            
        
        return newArr
            