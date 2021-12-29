from typing import Optional


class Binary:
    __number_of_binaries = 0

    def __init__(self, number: Optional[int]):
        """
        Create a new empty Binary.

        :param number: The number of the binary or None to auto-calculate it.
        """
        from models.service import Service
        if number is None:
            self.number = Binary.__number_of_binaries
        else:
            self.number = number
        self.services: list[Service] = []
        Binary.__number_of_binaries += 1

    def __str__(self):
        return f"\n\n\t\tBinary n°{self.number} " \
               f"{self.services}"

    def __repr__(self):
        return self.__str__()
