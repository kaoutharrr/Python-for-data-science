def ft_statistics(*args, **kwargs) -> None:
    """
    Calculate and print the Mean, Median, Quartile, Standard Deviation,
    and Variance according to the requested kwargs.
    """

    data = [x for x in args if isinstance(x, (int, float))]
    data.sort()
    n = len(data)

    def mean(values):
        return sum(values)/len(values)

    def median(v):
        length = len(v)
        mid = length // 2
        return (v[mid - 1] + v[mid]) / 2 if length % 2 == 0 else v[mid]

    def quartile_calc(v):
        """Calculate Q1 (25%) and Q3 (75%) quartiles using simple indexing."""
        length = len(v)
        q1_index = length // 4
        q3_index = 3 * length // 4

        return [float(v[q1_index]), float(v[q3_index])]

    def variance(v, m):
        return sum((x - m) ** 2 for x in v) / len(v)

    def std(v, var):
        return var ** 0.5

    if n == 0:
        if any(kwargs.values()):
            for val in kwargs.values():
                print("ERROR")
        return

    mean_val = mean(data)
    var_val = variance(data, mean_val)
    std_val = std(data, var_val)

    for val in kwargs.values():
        if val == "mean":
            print(f"mean: {mean_val}")
        elif val == "median":
            print(f"median: {median(data)}")
        elif val == "quartile":
            print(f"quartile: {quartile_calc(data)}")
        elif val == "var":
            print(f"var: {var_val}")
        elif val == "std":
            print(f"std: {std_val}")
