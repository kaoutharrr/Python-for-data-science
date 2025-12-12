from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing a King with multiple inheritance (Diamond problem)."""
    def __init__(self, first_name, is_alive=True):
        """Initialize a King character."""
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """Get the eye color of the King"""
        return self.eyes

    def get_hairs(self):
        """Get the hair color of the King"""
        return self.hairs

    def set_eyes(self, color):
        """Set the eye color of the King"""
        self.eyes = color

    def set_hairs(self, color):
        """Set the hair color of the King"""
        self.hairs = color
