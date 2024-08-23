# bin search + prefix sum and perhaps a range query data structure?
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        
        s_list = list(map(int, s))
        psum_0 = list(accumulate(s_list, lambda accumulated, element: accumulated + (element == 0), initial=int(s_list[0]==0)))
        psum_1 = list(accumulate(s_list, lambda accumulated, element: accumulated + element, initial=int(s_list[1]==1)))

        def q(start, end, d):
            if d == 0:
                if start == 0:
                    return psum_0[end]
                return psum_0[end] - psum_0[start-1]
            if start == 0:
                return psum_1[end]
            return psum_1[end]-psum_1[start-1]

        def valid(start, end):
            return q(start, end, 0) <= k and q(start, end, 1) <= k

        
        def right_invalid_start(l):
            left, right = l, len(s_list)
            res = -1
            while left <= right:
                mid = (left+right)//2
                if not valid(left, mid):
                    right = mid
                    res = mid - 1
                else:
                    left = mid + 1
            return res


            

        
                    
            