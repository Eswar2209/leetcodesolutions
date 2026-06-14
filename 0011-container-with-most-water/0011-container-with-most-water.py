class Solution(object):
    def maxArea(self, height):
        l=0
        r=len(height)-1
        ans=0
        while l<r:
            h=min(height[l],height[r])
            w=r-l
            area=w*h
            ans=max(ans,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ans
