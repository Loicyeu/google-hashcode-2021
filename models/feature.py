from models.binary import Binary
from models.service import Service


class Feature:
    def __init__(self, name: str, difficulty: int, daily_users: int):
        from models.service import Service
        self.name = name
        self.difficulty = difficulty
        self.daily_users = daily_users
        self.services: list[Service] = []
        self.implemented_services: set[Service] = set()

    def __copy__(self):
        return Feature(self.name, self.difficulty, self.daily_users)

    def __str__(self):
        return f"\n\t\t\t\tFeature {self.name}\n\t\t\t" \
               f"\t - Difficulty : {self.difficulty}\n\t\t\t" \
               f"\t - Daily users : {self.daily_users}"

    def __repr__(self):
        return self.__str__()

    def get_binaries(self) -> list[Binary]:
        """
        Get all binaries where the feature must be implemented_services

        :return: A list without duplicates
        """
        from utils import remove_duplicates
        return remove_duplicates([s.binary for s in self.services])

    def get_implemented_services(self) -> set[Service]:
        """
        Get all services where the feature is implemented_services

        :return: List of service
        """
        return self.implemented_services

    def get_remaining_binaries(self) -> set[Binary]:
        return set([s.binary for s in self.get_remaining_services()])

    def get_remaining_services(self) -> set[Service]:
        """
        Get all remaining services where the feature is not yet implemented_services

        :return: List of service
        """
        return set.difference(set(self.services), self.implemented_services)
