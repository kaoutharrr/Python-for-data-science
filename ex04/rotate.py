import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def ft_transpose(arr: np.ndarray) -> np.ndarray:
    """transpose an img"""
    rows, cols = arr.shape
    trans = np.zeros((cols, rows), dtype=arr.dtype)
    for i in range(rows):
        for j in range(cols):
            trans[j, i] = arr[i, j]
    return trans


def main():
    """loads an image , cut a square part from it and transpose it """

    try:
        img = ft_load("animal.jpeg")
        if img is None:
            return
        print(img)
        zoomed = img[100:500, 450:850, 0]
        arr = ft_transpose(zoomed)
        print(f"New shape after Transpose: {arr.shape}")
        print(arr)
        plt.imshow(arr, cmap='gray')
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
