import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """truncates a 2d array and return its new shape"""

    try:
        assert isinstance(family, list), "INPUT IS NOT A LIST!"
        arr = np.array(family)
        assert arr.ndim == 2, "List rows are not the same size or not 2D"
        print(f"My shape is : {arr.shape}")
        new_arr = arr[start:end]
        print(f"My new shape is : {new_arr.shape}")
        return new_arr.tolist()
    except Exception as e:
        print(f"ERROR : {e}")
