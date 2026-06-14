class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst=[c.lower()for c in s if c.isalnum()]
        
        return lst == lst[::-1]
        


        