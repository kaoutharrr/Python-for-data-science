import sys
from ft_filter import ft_filter


def main():
    """filter words from a string that are longer than a given length
    """
    try:
        args = sys.argv
        if len(args) != 3:
            raise AssertionError("the arguments are bad")
        text = args[1]
        try:
            n = int(args[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        words = text.split()
        res = ft_filter(lambda x: len(x) > n, words)
        print(list(res))

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
