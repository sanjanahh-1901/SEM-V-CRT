#Leetcode 1763: Longest Nice Substring
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        
        uniq = set(s)
        for i, ch in enumerate(s):
            if ch.lower() in uniq and ch.upper() in uniq:
                continue

            left = self.longestNiceSubstring(s[:i])
            right = self.longestNiceSubstring(s[i+1:])

            return left if len(left) >= len(right) else right
        
        return s