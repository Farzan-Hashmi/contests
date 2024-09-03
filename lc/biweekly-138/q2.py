from functools import cache


class Solution:
    def stringHash(self, s: str, k: int) -> str:

        @cache
        def to_int(c):
            lets = "abcdefghijklmnopqrstuvwxyz"
            return lets.index(c)

        @cache
        def to_char(i):
            lets = "abcdefghijklmnopqrstuvwxyz"
            return lets[i]

        n = len(s)
        MOD = 26
        windows = []
        res = []
        r = k - 1
        while r < len(s):
            windows.append(s[r - k + 1 : r + 1])
            r += k

        for window in windows:
            res.append(to_char(sum(to_int(c) for c in window) % MOD))

        return "".join(res)
