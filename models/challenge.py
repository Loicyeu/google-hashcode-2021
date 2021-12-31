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

    def get_score(self, features: list[Feature], engineers: list[Engineer]) -> int:
        for f in features:
            print(f"Feature {f.name} is implemented in ({len(f.get_implemented_services())}):")
            for ss in f.get_implemented_services():
                print(f"\t - {ss.name}")
            print(f"Feature {f.name} is not implemented in ({len(f.get_remaining_services())}):")
            for ss in f.get_remaining_services():
                print(f"\t - {ss.name}")
        print()
        for e in engineers:
            print(f"Engineer {e.id} finished in {e.days_past} days.")
            for a in e.actions:
                print(f"\t - {a}")
        return 0
