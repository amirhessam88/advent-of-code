from typing import TextIO


def _clean_test_data(file: TextIO) -> list[str]:
    """Returns cleaned input data.

    Parameters
    ----------
    file : str
        Input file

    Returns
    -------
    list[str]
    """
    return [line.rstrip() for line in file]
