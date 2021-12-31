from models.engineer import Engineer


class Engineers:
    def __init__(self, number, days_for_binary, challenge_days):
        self.engineers: list[Engineer] = [Engineer(i, days_for_binary) for i in range(number)]
        self.challenge_days: int = challenge_days

    def get_engineer(self) -> Engineer:
        self.engineers.sort(key=lambda e: e.days_past)
        return self.engineers[0]

    def get_all(self) -> list[Engineer]:
        self.engineers.sort(key=lambda e: e.id)
        return self.engineers

    def finished(self) -> bool:
        """

        :return: True if all days_past of engineers exceed the number of days of the challenge, False instead.
        """
        for e in self.engineers:
            if e.days_past < self.challenge_days:
                return False
        return True
