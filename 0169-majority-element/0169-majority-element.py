class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        max=None
        for num in nums:
            if count == 0:
                max=num
            if num == max:
                count += 1
            else:
                count -= 1
        return max