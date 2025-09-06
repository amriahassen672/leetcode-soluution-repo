class Solution(object):
    def twoSum(self, nums, target):
       numMap = {}
       n = len(nums)
       for number in range(n):
        complement = target - nums[number]
        if complement in numMap:
            return[numMap[complement], number]
        numMap[nums[number]] = number 
