import numpy as np
import matplotlib.image as mpimg


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image from the given path, prints its shape and pixel content,
    and returns the pixel array. Handles JPG and JPEG formats and errors.
    """
    if not path.lower().endswith(('.jpg', '.jpeg')):
        print("Error: File format must be JPG or JPEG.")
        return None
    try:
        img_arr = mpimg.imread(path)
        print(f"The shape of image is: {img_arr.shape}")
        print(img_arr)
        return img_arr
    except Exception as e:
        print(f"error : {e} ")
