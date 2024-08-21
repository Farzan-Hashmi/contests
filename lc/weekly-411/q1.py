from collections import Counter


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        
        def eligible(arr):
            return Counter(arr)["1"] <= k or Counter(arr)["0"] <= k
        
        return sum(1 if eligible(s[l:r]) else 0 for l in range(len(s)) for r in range(l+1, len(s)+1))
    
