class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i = 0      # Left pointer of the window
        ans = 0    # Maximum length found
        
        for j in range(len(s)):  # Right pointer expanding the window
            # If duplicate detected, shrink window from left until duplicate is removed
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
                
            seen.add(s[j])
            ans = max(ans, j - i + 1)
            
        return ans
        