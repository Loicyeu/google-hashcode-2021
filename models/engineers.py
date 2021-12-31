from models.engineer import Engineer


class Engineers:
    def __init__(self, number, days_for_binary):
        self.engineers: list[Engineer] = [Engineer(i, days_for_binary) for i in range(number)]

    def get_engineer(self) -> Engineer:
        self.engineers.sort(key=lambda e: e.days_past)
        return self.engineers[0]

    def get_all(self) -> list[Engineer]:
        self.engineers.sort(key=lambda e: e.id)
        return self.engineers
