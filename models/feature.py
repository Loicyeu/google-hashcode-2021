class Feature:
    def __init__(self, name: str, difficulty: int, daily_users: int):
        self.name = name
        self.difficulty = difficulty
        self.daily_users = daily_users
        self.services = []
