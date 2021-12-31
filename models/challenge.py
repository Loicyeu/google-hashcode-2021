from models.engineer import Engineer
from models.feature import Feature


class Challenge:

    def __init__(self, days: int, engineers: int, nb_features: int, nb_services: int, days_for_binary: int):
        from models.binary import Binary
        self.days = days
        self.engineers = engineers
        self.days_for_binary = days_for_binary
        self.binaries: list[Binary] = []
        self.nb_features = nb_features
        self.nb_services = nb_services

    def __str__(self):
        string = f"\nChallenge\n" \
                 f" - Days : {self.days}\n" \
                 f" - Engineers : {self.engineers}\n" \
                 f" - Days for bin : {self.days_for_binary}" \
                 f"{self.binaries}"
        string = string.replace("[", '')
        string = string.replace("]", '')
        string = string.replace(",", '')
        return string

    def get_score(self, features: list[Feature]) -> int:
        score = 0
        for feature in features:
            if len(feature.get_remaining_services()) == 0:
                score += feature.daily_users * max(0, self.days - feature.last_day_implemented)
        return score

    @staticmethod
    def print_trace(features: list[Feature], engineers: list[Engineer]):
        for f in features:
            len_impl = len(f.get_implemented_services())
            len_total = len(f.services)
            print(f"Feature {f.name} is implemented in ({len_impl}/{len_total}):")
            for ss in f.get_implemented_services():
                print(f"\t + {ss.name} (bin{ss.binary.number})")
            for ss in f.get_remaining_services():
                print(f"\t - {ss.name} (bin{ss.binary.number})")
        print()
        for e in engineers:
            print(f"Engineer {e.id} finished in {e.days_past} days.")
            for a in e.actions:
                print(f"\t - {a}")
