class Challenge:
    def __init__(self, days: int, engineers: int, days_for_binary: int, nb_features: int, nb_services: int):
        self.days = days
        self.engineers = engineers
        self.days_for_binary = days_for_binary
        self.binaries = []
        self.nb_features = nb_features
        self.nb_services = nb_services
