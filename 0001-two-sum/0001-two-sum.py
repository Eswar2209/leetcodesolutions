class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            r = target - n
            if r in d:
                return [d[r], i]
            d[n] = i