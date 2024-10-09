class Solution(object):
    def twoSum(self, numbers, target):
        front = 0
        back = len(numbers) - 1
        for number in numbers:
            if (numbers[front] + numbers[back] > target):
                back -= 1
            elif (numbers[front] + numbers[back] < target):
                front += 1
            else :
                return [front+1, back+1]

        
