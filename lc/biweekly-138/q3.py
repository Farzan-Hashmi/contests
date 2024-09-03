from itertools import permutations
import math


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        pals = set()

        def tupilator(s):
            l = [0 for _ in range(10)]
            for dig in s:
                l[int(dig)] += 1
            return tuple(l)

        def dp(index, state, start):
            if n % 2 == 0 and index == (n // 2):
                str_num = "".join(state)
                combined = str_num + str_num[::-1]
                if int(combined) % k == 0:
                    pals.add(tupilator(combined))
                return
            if n % 2 == 1 and index == (n // 2) + 1:
                str_num = "".join(state)
                str_num_half = str_num[: len(str_num) - 1]
                combined = str_num + str_num_half[::-1]
                if int(combined) % k == 0:
                    pals.add(tupilator(combined))
                return

            for i in range(0 + (start == True), 10):
                state_copy_list = list(state)
                state_copy_list.append(str(i))
                dp(index + 1, tuple(state_copy_list), False)

        dp(0, (), True)

        def perms(tup):
            n = sum(tup)
            fac = 1
            for element in tup:
                if element == 0:
                    continue
                fac *= math.factorial(element)

            return math.factorial(n) // fac

        def start_zero(tup):
            if tup[0] == 0:
                return 0
            l = list(tup)
            l[0] -= 1
            n = sum(l)
            return perms(tuple(l))

        res = 0
        for pal in pals:
            res += perms(pal) - start_zero(pal)

        return res
