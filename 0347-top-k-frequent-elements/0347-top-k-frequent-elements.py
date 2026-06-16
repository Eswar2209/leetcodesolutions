class Solution(object):
    def topKFrequent(self, nums, k):
        count=Counter(nums)
        ans=[]
        for num,freq in count.most_common(k):
            ans.append(num)
        return ans