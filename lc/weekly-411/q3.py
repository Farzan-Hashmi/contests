#sigh tle but time complexity should be optimal. python skill issue?

class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        
        ref_arrr = [pow(10, n-i-1, k) for i in range(n)]

        def ref_arr(index):
            return ref_arrr[index]
            
        res_arr = [0 for _ in range(n)]
        digs = [i for i in range(10)]
        digs.reverse()

        cachee = [[[-1 for _ in range(10)] for _ in range(10)] for _ in range(n)]

        def is_eligible(left, val, running_mod):
            right = n - left - 1
            if cachee[left][val][running_mod] != -1:
                return cachee[left][val][running_mod]
            if right - left == 1:
                return ((running_mod + val*(ref_arr(left) % k) + val*ref_arr(right)) % k) == 0
            if left == right:
                return (running_mod + val*(ref_arr(left) % k)) % k == 0
            for dig in digs:
                new_running_mod = (running_mod + val*(ref_arr(left) % k) + val*ref_arr(right) % k) % k
                if is_eligible(left+1, dig, new_running_mod):
                    cachee[left][val][running_mod] = True
                    return True
            cachee[left][val][running_mod] = False
            return False

        rm = 0
        for start in range(n//2+1):
            end = n - start - 1
            if end < start:
                break
            for d in digs:
                if is_eligible(start, d, rm):
                    res_arr[start] = d
                    res_arr[end] = d
                    rm = (rm + d*ref_arr(start) % k + d*ref_arr(end) %k) % k
                    break


        return "".join([str(e) for e in res_arr])

            
            
                
            
            
        
        
            

        