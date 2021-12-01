class Service:
    from models.binary import Binary

    def __init__(self, name: str, binary: Binary):
        from models.feature import Feature
        from models.binary import Binary
        self.name = name
        self.features: list[Feature] = []
        self.binary: Binary = binary

    def __str__(self):
        return f"\n\t\t - Service {self.name} " \
               f"{self.features}"

    def __repr__(self):
        return self.__str__()
