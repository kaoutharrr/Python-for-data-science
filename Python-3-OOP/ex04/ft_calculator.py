class calculator:
    """Calculator class for vector-vector operations using static methods."""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """ Calculate and print the dot product of two vectors."""
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {int(result)}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors element-wise and print the result"""
        result = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract two vectors element-wise and print the result."""
        result = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
