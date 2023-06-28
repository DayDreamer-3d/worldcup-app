"""
Utilities functions related to sequences.
"""


def remove_fields(
    sequence: list | dict, fields: list[str],
) -> list | dict:

    for ind, _ in enumerate(sequence):
        for f in fields:
            if getattr(sequence[ind], f):
                delattr(sequence[ind], f)
    return sequence


