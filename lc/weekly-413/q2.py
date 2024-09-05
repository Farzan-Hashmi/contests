from sortedcontainers import SortedList


class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:

        sl = SortedList(key=lambda x: abs(x[0]) + abs(x[1]))
        res = []

        for x, y in queries:
            sl.add((x, y))
            if len(sl) < k:
                res.append(-1)
            else:
                # you also just never pop and index k-1
                while len(sl) > k:
                    sl.pop()
                res.append(abs(sl[-1][0]) + abs(sl[-1][1]))

        return res
