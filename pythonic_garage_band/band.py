from abc import ABC, abstractmethod


class Band:
    """
    This class is a stand alone class, that has attributes and methods.

    it also has magic methods: (__init__) , (__str__) , (__repr__) to help with defining the attributes
    and make a representation of all instances of this class.

    the functionality of this class is that it should return a list of all previously created band instances
    using (to_list) method by appending the instances into a list called (instances).

    it also has a method (play_solos()) that loops through a created class list called (members) and calls
    another method (play_solo()) -which is defined in later classes below- for each on of them.

    """

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

    """
    This class is a super class or a parent class, that has attributes and methods.

    it also has magic methods: (__init__) , (__str__) , (__repr__) to help with defining the attributes
    and make a representation of all instances of this class.

    other classes (Guitarist, Bassist, Drummer) inherit from this class, and they have access to all its
    attributes and methods ----> that's am using @abstractmethod because for some methods I don't want to
    work on them here from the super class but rather, let each child class define them as it suits it.
    Those methods are below and have @abstractmethod written above them.

    """

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

    """
    This class is a child class, that gets its attributes and methods by inherting from Musician class.

    it also has magic methods: (__init__) , (__str__) , (__repr__) to help with defining the attributes
    and make a representation of all instances of this class.

    here I'm defining each method the Guitarist class inherted from the super class (Musician), in the way that
    best suits this class alone. Taking into count that the Guitarist instrument is "guitar".

    """

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

    """
    This class is a child class, that gets its attributes and methods by inherting from Musician class.

    it also has magic methods: (__init__) , (__str__) , (__repr__) to help with defining the attributes
    and make a representation of all instances of this class.

    here I'm defining each method the Bassist class inherted from the super class (Musician), in the way that
    best suits this class alone. Taking into count that the Bassist instrument is "bass".

    """

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

    """
    This class is a child class, that gets its attributes and methods by inherting from Musician class.

    it also has magic methods: (__init__) , (__str__) , (__repr__) to help with defining the attributes
    and make a representation of all instances of this class.

    here I'm defining each method the Drummer class inherted from the super class (Musician), in the way that
    best suits this class alone. Taking into count that the Drummer instrument is "drums".

    """

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
