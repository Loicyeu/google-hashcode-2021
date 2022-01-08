from __future__ import annotations

from typing import Optional

from models.feature import Feature


class Features:

    def __init__(self, features: list[Feature]):
        self.features: list[Feature] = features
        self.remaining: list[Feature] = features.copy()

    def next_one(self) -> Optional[Feature]:
        if len(self.remaining) == 0:
            return None
        return self.remaining[0]

    def next(self, nb: int = 1) -> Feature | list[Feature]:
        """
        Return the next features to implement

        :return: The next features
        """
        return self.remaining[0:nb]

    def get_all(self) -> list[Feature]:
        return self.features

    def set_done(self, f: Feature):
        self.remaining.remove(f)
