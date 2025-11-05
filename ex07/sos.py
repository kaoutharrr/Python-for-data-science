import sys


def main():
    """Convert a string to Morse code."""

    try:
        s = sys.argv
        if len(s) != 2:
            raise AssertionError("the arguments are bad")

        NESTED_MORSE = {
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
            "E": ".", "F": "..-.", "G": "--.", "H": "....",
            "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
            "M": "--", "N": "-.", "O": "---", "P": ".--.",
            "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
            "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
            "Y": "-.--", "Z": "--..",
            "0": "-----", "1": ".----", "2": "..---", "3": "...--",
            "4": "....-", "5": ".....", "6": "-....", "7": "--...",
            "8": "---..", "9": "----.",
            " ": "/"
        }

        res = []
        text = s[1].upper()
        for c in text:
            if c not in NESTED_MORSE:
                raise AssertionError("the arguments are bad")
            res.append(NESTED_MORSE[c])
        print(' '.join(res))

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
