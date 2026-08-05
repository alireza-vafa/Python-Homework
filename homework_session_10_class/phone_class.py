class Phone:

    def __init__(self, name, family, number, information):
        self.name = name.lower()
        self.family = family.lower()
        self.number = number
        self.information = information.lower()

    def __str__(self):
        return (
            f"{self.name:10}"
            f"{self.family:12}"
            f"{self.number:<12}"
            f"{self.information}"
        )