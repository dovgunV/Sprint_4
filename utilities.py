from random import choice
from string import ascii_lowercase, digits


class Generator:
    _OFFSET = 975

    @staticmethod
    def string(length: int = 2) -> str:
        return "".join(
            chr(ord(choice(ascii_lowercase)) + Generator._OFFSET)
            for _ in range(length)
        )

    @staticmethod
    def number(length: int = 12) -> int:
        return int("".join(choice(digits) for _ in range(length)))
