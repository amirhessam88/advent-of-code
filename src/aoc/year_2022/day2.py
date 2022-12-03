_MAPPING_1 = {
    "A Z": 0,
    "B X": 0,
    "C Y": 0,
    "A X": 3,
    "B Y": 3,
    "C Z": 3,
    "A Y": 6,
    "B Z": 6,
    "C X": 6,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

_MAPPING_2 = {
    "B X": 1,
    "C X": 2,
    "A X": 3,
    "A Y": 4,
    "B Y": 5,
    "C Y": 6,
    "C Z": 7,
    "A Z": 8,
    "B Z": 9,
}


def part1(data: list[str]) -> int:
    """Find the total score of the game based on the given scenarios.

    Parameters
    ----------
    data : list[str]
        Stream of data per line

    Returns
    -------
    int
    """
    total_score = 0
    for row in data:
        total_score += _MAPPING_1[row]
        total_score += _MAPPING_1[row[-1]]

    return total_score


def part2(data: list[str]) -> int:
    """Find the total score of the game based on the given scenarios.

    Parameters
    ----------
    data : list[str]
        Stream of data per line

    Returns
    -------
    int
    """
    total_score = 0
    for row in data:
        total_score += _MAPPING_2[row]

    return total_score
