import sys

try:
    n = sys.argv
    if len(n) == 1:
        sys.exit()
    assert len(n) <= 2, "more than one argument is provided"
    try:
        n = int(n[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    if n % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as e:
    print(f"AssertionError: {e}")
    
