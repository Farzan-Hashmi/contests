
#lmfao we do not need a seg tree for a q2 - still O(nlogn) tho.

from collections import defaultdict
from typing import List
import bisect


class SegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        rq = SegmentTree(nums)
        intervals = defaultdict(int)
        l = 0
        for r, element in enumerate(nums):
            if r == 0 or element - nums[r-1] == 1:
                intervals[l] = r
            else:
                l = r
                intervals[l]=r

        interval_list = list(intervals.keys())
        interval_list.sort()

        res = []
        l = 0
        r = l+k-1
        while r < len(nums):
            nearest_left = bisect.bisect_right(interval_list, l,)-1
            left_index, right_index = interval_list[nearest_left], intervals[interval_list[nearest_left]]
            if not left_index <= l <= r <= right_index:
                res.append(-1)
            else:
                res.append(rq.query(l, r+1))
            r+=1
            l+=1
        
        return res
            