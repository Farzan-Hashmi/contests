class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:

        letters = "abcdefgh"

        coord_to_color = defaultdict(int)

        for letter in letters:
            for i in range(1, 9):
                if (letters.index(letter) + 1) % 2 == 1:
                    if i % 2 == 1:
                        coord_to_color[(letter, i)] = "B"
                    else:
                        coord_to_color[(letter, i)] = "W"
                else:
                    if i % 2 == 1:
                        coord_to_color[(letter, i)] = "W"
                    else:
                        coord_to_color[(letter, i)] = "B"

        letter1, num1 = coordinate1[0], coordinate1[1]
        letter2, num2 = coordinate2[0], coordinate2[1]

        num1 = int(num1)
        num2 = int(num2)

        return coord_to_color[(letter1, num1)] == coord_to_color[(letter2, num2)]
