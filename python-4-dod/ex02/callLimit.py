
def callLimit(limit: int):
    """Decorator factory that limits the number of
    times a function can be called."""
    count = 0

    def callLimiter(function):
        """Decorator that wraps the function with call limiting."""

        def limit_function(*args, **kwds):
            """Wrapper function that enforces the call limit."""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, *kwds)
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
