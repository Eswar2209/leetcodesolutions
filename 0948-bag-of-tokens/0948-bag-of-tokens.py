class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        ans = 0
        while tokens:
            if power >= tokens[0]:
                power -= tokens.pop(0)
                score += 1
                ans = max(ans, score)
            elif score > 0 and len(tokens) > 1:
                power += tokens.pop()
                score -= 1
            else:
                break

        return ans