import sys


def main():
    """Main program: counts uppercase, lowercase, digits,
    punctuation, and spaces."""
    try:
        args = sys.argv
        assert len(args) <= 2, "more than one argument is provided"
        if (len(args) == 1):
            print("What is the text to count?")
            text = sys.stdin.read()
        else:
            text = args[1]
        uppers = lowers = puncts = digits = spaces = 0
        punctuation_chars = ".,;:!?\"'()-_[]{}<>@#$%^&*/\\|`~+="

        for c in text:
            if c.isupper():
                uppers += 1
            elif c.islower():
                lowers += 1
            elif c.isdigit():
                digits += 1
            elif c.isspace():
                spaces += 1
            elif c in punctuation_chars:
                puncts += 1

        print(f"The text contains {len(text)} characters:")
        print(f"{uppers} upper letters")
        print(f"{lowers} lower letters")
        print(f"{puncts} punctuation marks")
        print(f"{spaces} spaces")
        print(f"{digits} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
