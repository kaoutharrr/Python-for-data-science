from abc import ABC, abstractmethod


class Character(ABC):
    """abstract base class"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """constructor of character class"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """passes is_alive from True to False"""
        self.is_alive = False


class Stark(Character):
    """the concrete class named stark"""
    def __init__(self, first_name, is_alive=True):
        """initialises a stark family member"""
        super().__init__(first_name, is_alive)
