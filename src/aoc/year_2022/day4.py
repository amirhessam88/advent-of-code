def part1(data: list[str]) -> int:
    """Returns the total number of "fully" overlapped intervals.

    Parameters
    ----------
    data : list[str]
        Stream of data per line

    Returns
    -------
    int
    """
    total = 0
    for row in data:
        intervals = _get_intervals(row)
        t1, t2 = intervals[0], intervals[1]
        if (t1[0] <= t2[0] and t2[1] <= t1[1]) or (t1[0] >= t2[0] and t2[1] >= t1[1]):
            total += 1

    return total


def part2(data: list[str]) -> int:
    """Returns the total number of "partially" overlapped intervals.

    Parameters
    ----------
    data : list[str]
        Stream of data per line

    Returns
    -------
    int
    """
    total = 0
    for row in data:
        intervals = _get_intervals(row)
        t1, t2 = intervals[0], intervals[1]
        if (
            (t1[0] <= t2[1] and t1[0] >= t2[1])
            or (t1[1] >= t2[0] and t1[1] <= t2[1])
            or (t2[0] <= t1[1] and t2[0] >= t1[1])
            or (t2[1] >= t1[0] and t2[1] <= t1[1])
        ):
            total += 1

    return total


def _get_intervals(row: str) -> list[list[str]]:
    """Returns cleaned intervals.

    Returns
    -------
    list[list[str]]
    """
    intervals = []
    intervals.append(row.split(",")[0].split("-"))
    intervals.append(row.split(",")[1].split("-"))
    intervals = [list(map(int, l)) for l in intervals]  # type: ignore
    return intervals
