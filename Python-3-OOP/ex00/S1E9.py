from abc import ABC, abstractmethod


class Character(ABC):
    """abstract base class"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """constrctor of character class"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def something(self):
        """the abstract method"""
        pass

    def die(self):
        """passes is_alive from True to False"""
        self.is_alive = False


class Stark(Character):
    """the concrete class anmed stark"""
    def something(self):
        """This overrides the parent Character's 'something' method"""
        pass
