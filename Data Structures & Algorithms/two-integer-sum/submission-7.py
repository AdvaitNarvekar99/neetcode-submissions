class Solution:
    def twoSum(self, nums, target):
        myDict = {}  # value -> index

        for i, num in enumerate(nums):
            diff = target - num

            if diff in myDict:
                return [myDict[diff], i]

            myDict[num] = i