class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """for i in range(len(nums)) :
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target :
                    return [i,j] (bruteForce)"""
        dict={}
        for i,num in enumerate(nums) :
            compliment=target-num
            if compliment in dict :
                return[dict[compliment],i]
            dict[num]=i
                   