from models.binary import Binary
from models.service import Service


class Feature:
    """Represents a Feature of the challenge"""

    def __init__(self, name: str, difficulty: int, daily_users: int):
        """
        Creates a new feature.

        :param name: feature name
        :param difficulty: feature difficulty
        :param daily_users: feature daily users
        """
        from models.service import Service
        self.name: str = name
        self.difficulty: int = difficulty
        self.daily_users: int = daily_users
        self.services: list[Service] = []
        """List of services where the feature must be implemented (all services, implemented or not)"""
        self.implemented_services: set[Service] = set()
        """List of services where the feature is already implemented"""
        self.last_day_implemented: int = 0  # Test
        """The last day where an engineer worked on the feature"""

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
        Gets all binaries where the feature must be implemented (all binaries, implemented or not)

        :return: A list of binaries without duplicates
        """
        from utils.utils import remove_duplicates

        return remove_duplicates([s.binary for s in self.services])

    def get_remaining_binaries(self) -> set[Binary]:
        """
        Gets all remaining binaries where its services dont have the feature implemented

        :return: A set of binaries
        """
        return set([s.binary for s in self.get_remaining_services()])

    def get_remaining_services(self) -> set[Service]:
        """
        Gets all remaining services where the feature is not yet in implemented_services

        :return: List of services
        """
        return set.difference(set(self.services), self.implemented_services)
