def part1(data: list[str]) -> int:
    """Find the maximum of a stream of data.

    Parameters
    ----------
    data : list[str]
        Stream of data per line

    Returns
    -------
    int
    """
    current_max = 0
    calories = 0
    for row in data:
        if len(row):
            calories += int(row)
        else:
            current_max = max(calories, current_max)
            calories = 0

    return current_max


# TODO(amir): here I did the easy way; but the optimized way will be using deqeue prolly
# so, we can track three numbers and apply Kadane's algortihm on top of minimum of the three numbers
# so, we can pop out the minumum and push back the new max
def part2(data: list[str]) -> int:
    """Find the maximum of the top three stream of data.

    Parameters
    ----------
    data : list[str]
        Stream of data per line

    Returns
    -------
    int
    """
    maxs = []
    calories = 0
    for row in data:
        if len(row):
            calories += int(row)
        else:
            maxs.append(calories)
            calories = 0

    return sum(sorted(maxs, reverse=True)[:3])
