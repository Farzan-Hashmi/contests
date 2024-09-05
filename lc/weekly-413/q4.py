from functools import cache


class Solution:
    def maximumSubarrayXor(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:

        num_columns = len(nums)
        xorr = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]
        for i, element in enumerate(nums):
            xorr[0][i] = element

        num_columns -= 1
        curr_row = 1

        while num_columns > 0:
            for i in range(num_columns):
                xorr[curr_row][i] = xorr[curr_row - 1][i] ^ xorr[curr_row - 1][i + 1]
            curr_row += 1
            num_columns -= 1

        @cache
        def score(l, r):
            if l == r:
                return nums[l]
            length = r - l + 1
            curr = xorr[length - 1][l]
            return max(curr, score(l + 1, r), score(l, r - 1))

        res = []
        for s, e in queries:
            res.append(score(s, e))
        return res
