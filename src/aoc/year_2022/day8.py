def part1(data: list[str]) -> int:
    """Returns the the total number of visible trees from outside.

    Parameters
    ----------
    data : list[str]
        Stream of data per line

    Returns
    -------
    int
    """
    n_rows, n_cols = len(data), len(data[0])
    total = 0

    for i in range(n_rows):
        for j in range(n_cols):
            k = int(data[i][j])
            if (
                all(int(data[i][x]) < k for x in range(j))
                or all(int(data[i][x]) < k for x in range(j + 1, n_cols))
                or all(int(data[x][j]) < k for x in range(i))
                or all(int(data[x][j]) < k for x in range(i + 1, n_rows))
            ):
                total += 1

    return total


def part2(data: list[str]) -> int:
    """Returns the maximums scenic score among all trees.

    Parameters
    ----------
    data : list[str]
        Stream of data per line

    Returns
    -------
    int
    """
    n_rows, n_cols = len(data), len(data[0])
    score = 0

    for i in range(n_rows):
        for j in range(n_cols):
            k = int(data[i][j])
            left = right = up = down = 0

            for x in range(i - 1, -1, -1):
                up += 1
                if int(data[x][j]) >= k:
                    break

            for x in range(j - 1, -1, -1):
                left += 1
                if int(data[i][x]) >= k:
                    break

            for x in range(i + 1, n_rows):
                down += 1
                if int(data[x][j]) >= k:
                    break

            for x in range(j + 1, n_cols):
                right += 1
                if int(data[i][x]) >= k:
                    break

            score = max(score, up * down * right * left)

    return score
