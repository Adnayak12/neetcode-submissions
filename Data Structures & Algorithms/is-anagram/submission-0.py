class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        str_dict = {}
        for c in s:
            if c not in str_dict:
                str_dict[c] = 1
            else:
                str_dict[c] += 1
                
        for ch in t:
            if ch not in str_dict or str_dict[ch] == 0:
                return False
            if ch in str_dict:
                str_dict[ch] -= 1
        
        for val in str_dict.values():
            if val != 0:
                return False
        return True