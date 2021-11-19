class Binary:
    def __init__(self, number: int):
        from models.service import Service
        self.number = number
        self.services: list[Service] = []

    def __str__(self):
        return f"\n\n\t\tBinary n°{self.number} " \
               f"{self.services}"

    def __repr__(self):
        return self.__str__()
