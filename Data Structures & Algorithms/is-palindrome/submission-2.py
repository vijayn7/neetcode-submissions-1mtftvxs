class Solution:

    def valid(self, c):
        return 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9'

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:

            if not self.valid(s[l]):
                l += 1
            elif not self.valid(s[r]):
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        
        return True
            
