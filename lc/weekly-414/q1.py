class Solution:
    def convertDateToBinary(self, date: str) -> str:
        def dec_to_bin(x):
            x = int(x)
            return bin(x)[2:]

        individ = date.split("-")
        res = ""
        for element in individ:
            binn = dec_to_bin(element)
            res += binn
            res += "-"

        res = res[: len(res) - 1]
        return res
