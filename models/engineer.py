from models.binary import Binary
from models.feature import Feature
from models.service import Service
from models.writer import Writer


class Engineer:
    """
    Ne peut pas être interrompu lors d'une de ses taches
    """

    def __init__(self, id, days_for_binary):
        self.id: int = id
        self.days_for_binary = days_for_binary
        self.days_past = 0
        self.actions: list[str] = []
        self.writer: Writer = Writer()

    def implement(self, feature: Feature, binary: Binary):
        """
        Implement a feature in a specified binary on its services.

        :param feature: The feature to implement
        :param binary: The binary where to implement the feature.
        """
        days = feature.difficulty + len(binary.services) + binary.occuped[self.days_past]
        temp = set.intersection(set(binary.services), feature.services)
        feature.implemented_services = set.union(feature.implemented_services, temp)
        for i in range(self.days_past, self.days_past + days):
            binary.occuped[i] += 1
        self.days_past += days
        feature.last_day_implemented = max(feature.last_day_implemented, self.days_past)
        self.actions.append(f"impl {feature.name} {binary.number} in {days} days")
        self.writer.addTask(self.id, f"impl {feature.name} {binary.number}")

    def move_service(self, service: Service, binary: Binary):
        """
        Move the service from its binary to another binary.

        :param service: The service to move.
        :param binary: The targeted binary.
        """
        old_binary = service.binary
        self.days_past = max(len(old_binary.services), len(binary.services))
        service.binary = binary
        old_binary.services.remove(service)

    def create_binary(self) -> Binary:
        """
        Create a new Binary

        :return: The newly created binary
        """
        self.days_past += self.days_for_binary
        return Binary(None)

    def wait(self, days: int):
        self.days_past += days
