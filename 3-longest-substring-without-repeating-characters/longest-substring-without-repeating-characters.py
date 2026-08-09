class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {} 
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            char = s[right]
            
            # If character is inside the current window, move left pointer past it
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
                
            # Record/update the last seen position of the character
            char_map[char] = right
            
            # Calculate maximum window length seen so far
            max_len = max(max_len, right - left + 1)
            
        return max_len
            