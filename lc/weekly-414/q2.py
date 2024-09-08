class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:

        start.sort()

        def good(min_diff):
            start_cp = start.copy()
            for i in range(1, len(start_cp)):
                curr_value = start_cp[i]
                prev_value = start_cp[i - 1]
                if curr_value - prev_value <= min_diff:
                    diff = curr_value - prev_value
                    increase_amt = min_diff - diff
                    new_val = curr_value + increase_amt
                    if new_val > curr_value + d:
                        return False
                    start_cp[i] = new_val
            return True

        left, right = 0, 10**12
        boundary_index = -1

        while left <= right:
            mid = (left + right) // 2
            if not good(mid):
                boundary_index = mid
                right = mid - 1
            else:
                left = mid + 1

        return boundary_index - 1
