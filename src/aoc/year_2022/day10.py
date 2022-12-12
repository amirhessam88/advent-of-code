_CYCLES = {20, 60, 100, 140, 180, 220}
_WIDTH = 40
_HEIGHT = 6


def part1(data: list[str]) -> int:
    """Returns the the sum of the specific signal strengths.

    Parameters
    ----------
    data : list[str]
        Stream of data per line

    Returns
    -------
    int
    """
    x = 1
    cycle = 0
    total = 0

    for row in data:
        if row.split(" ")[0] == "noop":
            cycle += 1
            if cycle in _CYCLES:
                total += x * cycle
        elif row.split(" ")[0] == "addx":
            cycle += 1
            if cycle in _CYCLES:
                total += x * cycle
            cycle += 1
            if cycle in _CYCLES:
                total += x * cycle
            x += int(row.split(" ")[1])

    return total


def part2(data: list[str]) -> str:
    """Returns the letters on the CRT screen.

    Parameters
    ----------
    data : list[str]
        Stream of data per line

    Returns
    -------
    str
    """
    x = 1
    cycle = 0
    position = 0
    grid = [[" " for _ in range(_WIDTH)] for _ in range(_HEIGHT)]

    for row in data:
        if row.split(" ")[0] == "noop":
            cycle += 1
            grid, position = _updates(
                x=x,
                cycle=cycle,
                grid=grid,
                position=position,
            )
        elif row.split(" ")[0] == "addx":
            cycle += 1
            grid, position = _updates(
                x=x,
                cycle=cycle,
                grid=grid,
                position=position,
            )
            cycle += 1
            grid, position = _updates(
                x=x,
                cycle=cycle,
                grid=grid,
                position=position,
            )
            x += int(row.split(" ")[1])

    return _render_grid(
        grid=grid,
    )


def _updates(
    x: int,
    cycle: int,
    grid: list[list[str]],
    position: int,
) -> tuple[list[list[str]], int]:
    """Returns updated grid and position once rendered time.

    Parameters
    ----------
    x : int
        X value

    cycle : int
        Cycle iteration

    grid : list[list[str]]
        Grid to show letters

    position : int
        Current position

    Returns
    -------
    tuple[list[list[str]], int]
        Updated grid and position
    """
    _cycle = cycle - 1
    grid[_cycle // _WIDTH][_cycle % _WIDTH] = "#" if abs(x - (_cycle % _WIDTH)) <= 1 else "."
    if cycle in _CYCLES:
        position += x * cycle

    return grid, position


def _render_grid(grid: list[list[str]]) -> str:
    """Renders the letters in the grid to be readable.

    Parameters
    ----------
    grid : list[list[str]]
        Grid of letters

    Returns
    -------
    str
    """
    letters = "\n"
    for i in range(_HEIGHT):
        letters += "".join(grid[i])
        letters += "\n"

    return letters
