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
