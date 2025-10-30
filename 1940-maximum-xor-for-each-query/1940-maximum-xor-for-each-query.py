class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        result=[]
        xor_all=0
        for num in nums :
            xor_all^=num
        mask =(1<<maximumBit)-1
        for i in range (len(nums)) :
            result.append(xor_all^mask)
            xor_all^=nums[-1-i]
        return result
