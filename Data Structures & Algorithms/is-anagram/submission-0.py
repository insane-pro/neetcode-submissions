class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count={}
        for i in range(len(s)):
            char_count[s[i]]=char_count.get(s[i],0)+1
            char_count[t[i]]=char_count.get(t[i],0)-1
        return all(v ==0 for v in char_count.values())
            
            
    
    
