from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """loads the img , print information about it,
    and display it after zooming """
    try:
        img_arr = ft_load("animal.jpeg")
        if img_arr is None:
            return
        zoomed = img_arr[100:500, 450:850, 0]
        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)
        plt.imshow(zoomed, cmap='gray')
        plt.title('Zoomed Raccoon Face')
        plt.xlabel('X-axis scale')
        plt.ylabel('Y-axis scale')
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
