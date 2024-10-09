class Solution(object):
    def sortColors(self, nums):
        currentPointer = 0
        zeroSwap = 0
        twoSwap = len(nums)-1
        while currentPointer <= twoSwap:
            if nums[currentPointer] == 0:
                nums[currentPointer], nums[zeroSwap] = nums[zeroSwap], nums[currentPointer]
                zeroSwap += 1
                currentPointer += 1
            elif nums[currentPointer] == 1:
                currentPointer += 1
            else :
                nums[currentPointer], nums[twoSwap] = nums[twoSwap], nums[currentPointer]
                twoSwap -= 1

        
