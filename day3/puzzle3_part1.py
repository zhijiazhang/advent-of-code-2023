def solve(filename: str) -> int:

    with open(filename) as reader:
        matrix = reader.readlines()
        rows, cols = len(matrix), len(matrix[0])
        seen = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        total = 0

        for i in range(rows):
            for j in range(cols):
                if not matrix[i][j].isnumeric() and matrix[i][j] != "." and matrix[i][j] != "\n":
                    for r,c in directions:
                        ni, nj = i + r, j + c

                        if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj].isnumeric():
                                row = matrix[ni]
                                s , e = nj, nj
                                while s >= 0 and (row[s].isnumeric()): s -= 1
                                while e < cols and (row[e].isnumeric()): e += 1
                                s += 1
                                e -= 1

                                if ((ni, s)) not in seen:
                                    seen.add((ni, s))
                                    total += int(matrix[ni][s : e + 1])
    return total