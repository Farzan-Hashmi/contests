class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:

        location_to_val = defaultdict(int)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                location_to_val[(r, c)] = grid[r][c]

        items = list(location_to_val.items())

        items.sort(key=lambda x: x[1], reverse=True)

        def bin_search(val):
            l = 0
            r = len(items) - 1
            res = len(items)
            while l <= r:
                mid = (l + r) // 2
                if items[mid][1] < val:
                    res = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return res

        print(items)

        @cache
        def dp(index, seen_rows):
            if index == len(items):
                return 0

            curr_row = items[index][0][0]
            if seen_rows & (1 << curr_row):
                return dp(index + 1, seen_rows)

            curr_val = items[index][1]
            next_index = bin_search(curr_val)
            return max(
                curr_val + dp(next_index, seen_rows | (1 << curr_row)),
                dp(index + 1, seen_rows),
            )

        return dp(0, 0)
