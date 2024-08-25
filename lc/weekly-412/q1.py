from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            min_val = min(nums)
            i = None
            for j, v in enumerate(nums):
                if v == min_val:
                    i = j
                    break
            
            nums[i] = nums[i] * multiplier
        
        return nums