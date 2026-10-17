class Solution:
    def isPalindrome(self, s: str) -> bool:
            seq = "".join([c.lower() for c in s if c.isalnum()])

            return seq == seq[::-1]