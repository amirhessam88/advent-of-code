import string

_MAPPING = dict(
    [
        (v, k)
        for k, v in dict(
            enumerate(
                string.ascii_letters,
                1,
            ),
        ).items()
    ],
)


def part1(data: list[str]) -> int:
    """Find the total sum of priorities of items in both compartments.

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
        total += _MAPPING[_get_priority_between_compartments(row)]

    return total


def part2(data: list[str]) -> int:
    """Find the total sum of priorities of items among three groups.

    Parameters
    ----------
    data : list[str]
        Stream of data per line

    Returns
    -------
    int
    """
    total = 0
    length = len(data) // 3
    for i in range(length):
        triplets = data[i * 3 : (i + 1) * 3]
        g1, g2, g3 = triplets[0], triplets[1], triplets[2]
        total += _MAPPING[_get_priority_between_groups(g1, g2, g3)]

    return total


def _get_priority_between_compartments(s: str) -> str:
    """Returns the common priority between two compartments.

    Parameters
    ----------
    s : str
        Items in both compartments

    Returns
    -------
    str
    """
    left, right = set(s[: len(s) // 2]), set(s[len(s) // 2 :])
    return (left & right).pop()


def _get_priority_between_groups(g1: str, g2: str, g3: str) -> str:
    """Returns the common priority between three groups.

    Parameters
    ----------
    g1 : str
        Group1 items

    g2 : str
        Group2 items

    g3 : str
        Group3 items

    Returns
    -------
    str
    """
    return (set(g1) & set(g2) & set(g3)).pop()
