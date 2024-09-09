class Solution:
    def countPairs(self, nums: List[int]) -> int:

        def gen(num):
            res = set()
            l = [d for d in num]
            for i in range(len(l)):
                for j in range(i + 1, len(l)):
                    l_copy = l.copy()
                    l_copy[i], l_copy[j] = l_copy[j], l_copy[i]
                    res.add("".join(l_copy))

            for i in range(len(l)):
                for j in range(i + 1, len(l)):
                    l_copy = l.copy()
                    l_copy[i], l_copy[j] = l_copy[j], l_copy[i]
                    for k in range(len(l)):
                        for m in range(k + 1, len(l)):
                            l_copy_two = l_copy.copy()
                            l_copy_two[k], l_copy_two[m] = l_copy_two[m], l_copy_two[k]
                            res.add("".join(l_copy_two))

            return res

        str_digits = [str(num) for num in nums]
        for i, str_digit in enumerate(str_digits):
            str_digits[i] = str_digit.zfill(7)

        hm = defaultdict(int)

        res = 0

        for str_digit in str_digits:
            other_possible = gen(str_digit)
            # print(str_digit, other_possible)
            for other in other_possible:
                res += hm[other]
            hm[str_digit] += 1

        return res
