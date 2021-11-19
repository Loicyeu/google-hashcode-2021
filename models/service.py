class Service:
    def __init__(self, name: str):
        from models.feature import Feature
        self.name = name
        self.features: list[Feature] = []

    def __str__(self):
        return f"\n\t\t - Service {self.name} " \
               f"{self.features}"

    def __repr__(self):
        return self.__str__()
