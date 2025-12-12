class calculator:
    """Calculator class for vector-scalar operations."""
    def __init__(self, vector):
        """initializes the calculator with a vector"""
        self.vector = vector

    def __add__(self, object) -> None:
        """add a scalar to each elem of the vect"""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """multiplay each elem of the vect by a scalar"""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """ Subtract a scalar from each elem of the vect"""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """ Divide each eleme of the vect by a scalar."""
        if object == 0:
            raise ValueError("Cannot divide by zero")
        self.vector = [x / object for x in self.vector]
        print(self.vector)
