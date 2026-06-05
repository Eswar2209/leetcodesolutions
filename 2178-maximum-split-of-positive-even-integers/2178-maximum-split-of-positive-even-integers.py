class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []
        ans = []
        curr = 2
        while finalSum >= curr:
            ans.append(curr)
            finalSum -= curr
            curr += 2
        ans[-1] += finalSum
        return ans