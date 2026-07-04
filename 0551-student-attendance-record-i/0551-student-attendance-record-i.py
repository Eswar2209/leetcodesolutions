class Solution:
    def checkRecord(self, s: str) -> bool:
        absent=0
        late=0
        for ch in s:
            if ch == 'A':
                absent += 1
                late=0
            elif ch == 'L':
                late += 1
            else:
                late = 0
            if absent >=2 or late >=3:
                return False
        return True