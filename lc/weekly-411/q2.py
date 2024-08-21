from functools import cache
from typing import List


class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:

        hm = {0: energyDrinkA, 1: energyDrinkB}
        
        @cache
        def dp(index, arr):
            if index >= len(energyDrinkA):
                return 0
            
            take_val = hm[arr][index] + dp(index+1, arr)
            switch = hm[arr][index] + dp(index+2, not arr)
            return max(take_val, switch)

        return max(dp(0,0), dp(0,1))