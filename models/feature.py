class Feature:
    def __init__(self, name: str, difficulty: int, daily_users: int):
        from models.service import Service
        self.name = name
        self.difficulty = difficulty
        self.daily_users = daily_users
        self.services: list[Service] = []

    def __str__(self):
        return f"\n\t\t\t\tFeature {self.name}\n\t\t\t" \
               f"\t - Difficulty : {self.difficulty}\n\t\t\t" \
               f"\t - Daily users : {self.daily_users}"

    def __repr__(self):
        return self.__str__()
