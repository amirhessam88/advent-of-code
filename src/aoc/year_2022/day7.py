from collections import defaultdict


def _traverse_directories(data: list[str]) -> dict[str, int]:
    """Returns the mapping of each directory with total size of the spaces.

    Parameters
    ----------
    data : list[str]
        Stream of data per line

    Returns
    -------
    dict[str, int]
    """
    spaces: dict[str, int] = defaultdict(int)
    tmp: list[str] = []

    for command in data:
        if command.split(" ")[1] == "cd":
            if command.split(" ")[2] == "..":
                tmp.pop()
            else:
                tmp.append(command.split(" ")[2])
        elif command.split(" ")[1] == "ls":
            continue
        else:
            try:
                space = int(command.split(" ")[0])
                for i in range(len(tmp) + 1):
                    spaces["/".join(tmp[:i])] += space
            except Exception:
                pass

    return spaces


def part1(data: list[str]) -> int:
    """Returns the the total size of directories at most 100000.

    Parameters
    ----------
    data : list[str]
        Stream of data per line

    Returns
    -------
    int
    """
    spaces = _traverse_directories(data)
    total = 0
    for _, v in spaces.items():
        if v <= 100000:
            total += v

    return total


def part2(data: list[str]) -> float:
    """Returns the size of smallest directoy to be free up to hit the limit.

    Parameters
    ----------
    data : list[str]
        Stream of data per line

    Returns
    -------
    float
    """
    spaces = _traverse_directories(data)
    ans = float("inf")

    TOTAL_SPACE = 70000000
    UNUSED_SPACE = 30000000
    MAX_USED_SPACE = TOTAL_SPACE - UNUSED_SPACE
    CURRENT_TOTAL = spaces["/"]
    TO_BE_DELETED = CURRENT_TOTAL - MAX_USED_SPACE

    for _, v in spaces.items():
        if v >= TO_BE_DELETED:
            ans = min(ans, v)

    return ans
