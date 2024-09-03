class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:

        def pad(str_num):
            if len(str_num) < 4:
                diff = 4 - len(str_num)
                return "0" * diff + str_num
            return str_num

        padded = [pad(str(num1)), pad(str(num2)), pad(str(num3))]

        res = ""
        for i in range(4):
            opts = []
            for padded_str in padded:
                opts.append(int(padded_str[i]))
            res += str(min(opts))

        return int(res)
