from functools import cache


class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        
        res_arr = [0 for _ in range(n)]

        def adder(val, index):
            return (val * pow(10, n - index - 1, k) ) % k

        @cache
        def dp(left, mod):
            right = n - left - 1
            if left > right:
                return mod == 0 
            for i in range(9,-1,-1):
                new_mod = (mod + adder(i, left) + adder(i, right)) % k if left != right else (mod + adder(i, left)) % k
                if dp(left+1, new_mod):
                    res_arr[left] = i
                    res_arr[right] = i
                    return True
            return False
        
        dp(0,0)
        return "".join([str(e) for e in res_arr])
            
            
        
        
            

        