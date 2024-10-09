class Solution(object):
    def productExceptSelf(self, nums):
        count = 0
        product = 1
        returnList = [0] * len(nums)
        zeroIndex = 0
        for num in nums:
            if num == 0:
                count += 1
            else:
                product *= num
        if count > 1:
            return returnList
        elif count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    zeroIndex = i
            returnList[zeroIndex] = product;
            return returnList
        else:
            for i in range(len(nums)):
                returnList[i] = product/nums[i]
            return returnList

    
