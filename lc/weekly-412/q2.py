
from typing import List


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        
        def is_almost_equal(num1, num2):
            num1str = list(map(str, str(num1)))
            num2str = list(map(str, str(num2)))

            if num1 == num2:
                return True

            for i in range(len(num1str)):
                for j in range(i+1, len(num1str)):
                    temp = num1str[::1]
                    temp[i], temp[j] = temp[j], temp[i]
                    if int("".join(temp)) == num2:
                        return True
            
            for i in range(len(num2str)):
                for j in range(i+1, len(num2str)):
                    temp = num2str[::1]
                    temp[i], temp[j] = temp[j], temp[i]
                    if int("".join(temp)) == num1:
                        return True
                
            
            return False


        
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                res += is_almost_equal(nums[i], nums[j])

        return res
