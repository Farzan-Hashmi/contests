class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:

        def is_valid(x, y):
            return 0 <= x < 50 and 0 <= y < 50

        @cache
        def min_moves(kx, ky, px, py):
            visited = [[False for _ in range(50)] for _ in range(50)]
            q = deque([(kx, ky, 0)])
            while q:
                currkx, currky, num_moves = q.popleft()
                if visited[currkx][currky]:
                    continue
                visited[currkx][currky] = True
                if currkx == px and currky == py:
                    return num_moves

                for dx, dy in [
                    (-2, 1),
                    (-2, -1),
                    (2, -1),
                    (2, 1),
                    (1, 2),
                    (1, -2),
                    (-1, 2),
                    (-1, -2),
                ]:
                    if is_valid(currkx + dx, currky + dy):
                        q.append((currkx + dx, currky + dy, num_moves + 1))

        @cache
        def bob(kx, ky, mask):
            if mask == 2 ** len(positions) - 1:
                return 0
            res = float("inf")
            for i in range(len(positions)):
                if not (mask & (1 << i)):
                    res = min(
                        res,
                        min_moves(kx, ky, positions[i][0], positions[i][1])
                        + alice(positions[i][0], positions[i][1], mask | (1 << i)),
                    )
            return res

        @cache
        def alice(kx, ky, mask):
            if mask == 2 ** len(positions) - 1:
                return 0
            res = -1
            for i in range(len(positions)):
                if not (mask & (1 << i)):
                    print(min_moves(kx, ky, positions[i][0], positions[i][1]))
                    res = max(
                        res,
                        min_moves(kx, ky, positions[i][0], positions[i][1])
                        + bob(positions[i][0], positions[i][1], mask | (1 << i)),
                    )
            return res

        return alice(kx, ky, 0)
