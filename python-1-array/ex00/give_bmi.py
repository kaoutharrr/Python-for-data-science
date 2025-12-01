import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """calculates the bmi value of two lists of integers"""
    try:
        assert len(height) == len(weight), "Lists should be the same size!"
        np_height = np.array(height)
        np_weight = np.array(weight)
        np_res = np_weight / (np_height ** 2)
        return (np_res.tolist())
    except Exception as e:
        print(f"Error :{e}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """checks if the elements of a list of bmi values are above the limit"""
    try:
        my_array = np.array(bmi)
        res = my_array > limit
        return res.tolist()

    except Exception as e:
        print(f"Error :{e}")
