def part1(data: list[str]) -> int:
    """Returns the the index of the first 4 non-repeated characters.

    Parameters
    ----------
    data : list[str]
        Stream of data per line

    Returns
    -------
    int
    """
    word = data[0]
    length = len(word)
    step = 4
    for i in range(length):
        cur = word[i : i + step]
        if len(set(cur)) == step:
            ans = i + step
            break
    return ans


def part2(data: list[str]) -> int:
    """Returns the the index of the first 14 non-repeated characters.

    Parameters
    ----------
    data : list[str]
        Stream of data per line

    Returns
    -------
    int
    """
    word = data[0]
    length = len(word)
    step = 14
    for i in range(length):
        cur = word[i : i + step]
        if len(set(cur)) == step:
            ans = i + step
            break
    return ans
