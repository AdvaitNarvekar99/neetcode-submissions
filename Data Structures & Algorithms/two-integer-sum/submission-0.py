class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        else:
            myDict = dict()
            for i in range(0, len(nums)):
                if nums[i] in list(myDict):
                    return(sorted([i, myDict[nums[i]]]))
                else:
                    myDict[target - nums[i]] = i