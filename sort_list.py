"""Utility to sort a list of integers in ascending order."""

from typing import List


def sort_integers(data: List[int]) -> List[int]:
    """Return a new list containing the integers from ``data`` sorted in ascending order.

    Parameters
    ----------
    data : List[int]
        The list of integers to sort.

    Returns
    -------
    List[int]
        A new list with the integers sorted in ascending order.

    Raises
    ------
    TypeError
        If ``data`` is not a list.
    """
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    # Use Python's built-in sorted to return a new sorted list
    return sorted(data)


if __name__ == "__main__":
    example = [3, 1, 4, 1, 5]
    print(sort_integers(example))
