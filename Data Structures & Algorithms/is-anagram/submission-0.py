class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sorted_str_s = "".join(sorted(s))
        sorted_str_t = "".join(sorted(t))

        if len(s) == len(t):
            # do sth
            if sorted_str_s == sorted_str_t:
                return True
        
        return False
        