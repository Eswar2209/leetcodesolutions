class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        ans=[1]*n
        lft=1
        for i in range(n):
            ans[i]=lft
            lft*=nums[i]

        rgt=1
        for i in range(n-1,-1,-1):
            ans[i]*=rgt
            rgt*=nums[i]
        return ans