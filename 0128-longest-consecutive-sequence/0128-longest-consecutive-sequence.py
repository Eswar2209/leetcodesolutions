class Solution(object):
    def longestConsecutive(self, nums):
        s=set(nums)
        ans=0
        for num in s:
            if num -1 not in s:
                count=0
                while num in s:
                    count += 1
                    num += 1
                ans=max(ans,count)
        return ans
