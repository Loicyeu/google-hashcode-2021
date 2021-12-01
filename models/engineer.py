from typing import Optional

from models.binary import Binary
from models.feature import Feature
from models.service import Service


class Engineer:
    """
    Ne peut pas être interrompu lors d'une de ses taches
    """

    def __init__(self, id):
        self.id: int = id
        self.free: bool = True
        self.feature: Optional[Feature] = None
        self.free_in: int = 0

    def implement(self, feature: Feature, binary: Binary):
        """
        Commence la réalisation d'un binaire ssi l'ingé est libre.

        :param feature: La feature a implémenter
        :param binary: Le binaire sur lequel faire la feature.
        :return:
        """
        pass

    def move_service(self, service: Service, binary: Binary):
        """
        Déplace le service de son binaire vers le binaire cible

        :param service: Le service a déplacer
        :param binary: Le binaire cible
        :return:
        """
        pass

    def create_binary(self):
        """
        Créer un nouveau binaire.

        :return:
        """
        pass

    def wait(self, days: int) -> bool:
        if self.free:
            self.free = False
            self.free_in = days
        else:
            raise Exception(f"L'ingénieur {self.id} est déjà occupé")
        # TODO: écrire dans le fichier de sortie
        return True
