class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # pointer for placing elements that are NOT equal to val
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # move non-val element to the front
                k += 1
        return k
