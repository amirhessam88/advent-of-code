_NUMBER_OF_STACKS = 9
_STACK_LENGTH = 3


def part1(data: list[str]) -> str:
    """Returns the last letter of each stack as a message.

    Parameters
    ----------
    data : list[str]
        Stream of data per line

    Returns
    -------
    str
    """
    stacks, steps = _parse_stacks(data), _parse_steps(data)
    for step in steps:
        _count, _from, _to = step
        for _ in range(_count):
            stacks[f"{_to}"].append(stacks[f"{_from}"].pop())

    message = ""
    for _, stack in stacks.items():
        message += stack[-1]

    return message.replace("[", "").replace("]", "")


def part2(data: list[str]) -> str:
    """Returns the last letter of each stack as a message while keeping the order of stacks inplaced.

    Parameters
    ----------
    data : list[str]
        Stream of data per line

    Returns
    -------
    str
    """
    stacks, steps = _parse_stacks(data), _parse_steps(data)
    for step in steps:
        _count, _from, _to = step
        _tmp = []
        for _ in range(_count):
            _tmp.append(stacks[f"{_from}"].pop())

        for _ in range(len(_tmp)):
            stacks[f"{_to}"].append(_tmp.pop())

    message = ""
    for _, stack in stacks.items():
        message += stack[-1]

    return message.replace("[", "").replace("]", "")


def _parse_stacks(data: list[str]) -> dict[str, list[str]]:
    """Returns the mapping of stacks of letters.

    Returns
    -------
    dict[str, list[str]]
    """
    stacks: dict[str, list[str]] = {f"{i+1}": [] for i in range(_NUMBER_OF_STACKS)}
    for row in data:
        if "1" not in row:
            cnt = 0
            idx_a, idx_b = 0, _STACK_LENGTH
            while cnt != _NUMBER_OF_STACKS:
                if row[idx_a:idx_b] and row[idx_a:idx_b][0] == "[":
                    stacks[f"{cnt+1}"].append(row[idx_a:idx_b])
                idx_a += 4
                idx_b += 4
                cnt += 1

    return {k: list(reversed(v)) for k, v in stacks.items()}


def _parse_steps(data: list[str]) -> list[list[int]]:
    """Returns the steps per lines.

    Returns
    -------
    list[list[int]]
    """
    steps = []
    for row in data:
        if "move" in row:
            step = []
            step.append(int(row.split(" ")[1]))
            step.append(int(row.split(" ")[3]))
            step.append(int(row.split(" ")[5]))
            steps.append(step)

    return steps
