class Solution:
    def maxSubArray(self, nums):
        cur = ans = nums[0]

        for i in range(1, len(nums)):
            if cur < 0:
                cur = nums[i]
            else:
                cur += nums[i]

            if cur > ans:
                ans = cur

        return ans