from abc import ABC, abstractmethod


class Band:

    instances = []
    members = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self):
        return f"This is {self.name} from Band class"

    def __repr__(self):
        return f"This is the representation of {self.name} from Band class"

    def play_solos(self):
        solos = []
        for i in self.members:
            solos.append(i.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return cls.instances


class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f"This is {self.name} from Musician class"

    def __repr__(self):
        return f"This is a representation of {self.name} from the Musician class"

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass


class Guitarist(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = "guitar"

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return f"{self.instrument}"

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = "bass"

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return f"{self.instrument}"

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = "drums"

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return f"{self.instrument}"

    def play_solo(self):
        return "rattle boom crash"


if __name__ == "__main__":
    # pink_floyd = Band("pink floyd","5")
    # pink_floyd = Bassist("pink floyd")
    # print(pink_floyd.play_solo())
    # the_nobodies = Band("The Nobodies", [])
    buckethead = Guitarist("buckethead")
    print(buckethead.get_instrument())
