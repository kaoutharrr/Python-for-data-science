import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    inverted = 255 - array
    plt.imshow(inverted)
    plt.show()
    return inverted


def ft_red(array) -> np.ndarray:
    """Keeps only red channel."""
    red = array * [1, 0, 0]
    plt.imshow(red)
    plt.show()
    return red


def ft_green(array) -> np.ndarray:
    """Keeps only green channel."""
    green = array - (array * [1, 0, 1])
    plt.imshow(green)
    plt.show()
    return green


def ft_blue(array) -> np.ndarray:
    """Keeps only blue channel."""
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    plt.imshow(blue)
    plt.show()
    return blue


def ft_grey(array) -> np.ndarray:
    """Converts to grayscale."""
    grey = array.sum(axis=2, keepdims=True)/3
    image = np.repeat(grey, 3, axis=2)
    image = image.astype(int)

    plt.imshow(image)
    plt.show()
    return image
