# Python for Data Science - Day 4: Data Oriented Design

## 📚 Overview

This module focuses on proper Python programming practices for data science, emphasizing clean code structure, functional programming concepts, and avoiding common pitfalls that data scientists often fall into.

**Key Learning Objectives:**
- Write clean, structured Python code with proper function organization
- Understand and implement closures and decorators
- Use dataclasses for clean data structure definitions
- Handle variable arguments (*args, **kwargs) effectively
- Implement proper error handling

---

## 🎯 Exercise 00: Calculate My Statistics

### Concept
Learn to work with variable arguments and implement statistical calculations dynamically based on keyword arguments.

### What You'll Build
A function `ft_statistics()` that:
- Accepts any number of values via `*args`
- Calculates different statistics based on `**kwargs` keys
- Supports: mean, median, quartile (25%, 75%), standard deviation, variance

### Key Concepts
- **`*args`**: Captures unlimited positional arguments as a tuple
- **`**kwargs`**: Captures unlimited keyword arguments as a dictionary
- **Error handling**: Gracefully handle empty data sets

### Example Implementation Approach
```python
def ft_statistics(*args: Any, **kwargs: Any) -> None:
    # Check if args is empty
    # For each key in kwargs:
    #   - If key == "mean": calculate and print mean
    #   - If key == "median": calculate and print median
    #   - etc.
```

### Learning Points
- Statistical formulas implementation
- Dynamic function behavior based on kwargs
- Handling edge cases (empty input)

---

## 🎯 Exercise 01: Outer Inner (Closures)

### Concept
Understanding **closures** - functions that remember values from their enclosing scope even after the outer function has finished executing.

### What You'll Build
Three functions:
1. `square(x)` - returns x²
2. `pow(x)` - returns x^x
3. `outer(x, function)` - returns a closure that applies the function repeatedly

### How Closures Work
```python
def outer(x, function):
    count = 0
    def inner():
        nonlocal count  # Access outer function's variable
        # Apply function to x, update x
        # Increment count
        # Return result
    return inner
```

### The Magic
When you call `outer(3, square)`:
- It returns the `inner` function
- `inner` remembers `x` and `function` 
- Each call to `inner()` applies the function and updates the result
- `3 → square(3) = 9 → square(9) = 81 → square(81) = 6561`

### Learning Points
- Closures capture and maintain state
- `nonlocal` keyword for modifying outer scope variables
- Functional programming patterns

---

## 🎯 Exercise 02: Call Limit Decorator

### Concept
**Decorators** - functions that modify the behavior of other functions. They're a powerful Python feature for adding functionality without changing the original function.

### What You'll Build
A decorator that limits how many times a function can be called:

```python
@callLimit(3)
def f():
    print("f()")
```

### How Decorators Work
Decorators use a three-layer structure:
```python
def callLimit(limit):              # 1. Accepts decorator parameters
    def callLimiter(function):     # 2. Accepts the function to decorate
        def limit_function(*args, **kwds):  # 3. Wrapper that adds behavior
            # Check if call count < limit
            # If yes: call function
            # If no: print error
        return limit_function
    return callLimiter
```

### The Process
1. `@callLimit(3)` calls `callLimit(3)`, which returns `callLimiter`
2. `callLimiter` receives function `f` and returns `limit_function`
3. Now when you call `f()`, you're actually calling `limit_function()`

### Learning Points
- Triple-nested function pattern for parametrized decorators
- `*args, **kwargs` for preserving function signatures
- Practical use case: rate limiting, access control

---

## 🎯 Exercise 03: Dataclass

### Concept
**Dataclasses** - Python's modern way to create classes that primarily store data. They automatically generate boilerplate methods like `__init__`, `__repr__`, and `__eq__`.

### What You'll Build
A `Student` dataclass with:
- Settable fields: `name`, `surname`, `active` (defaults to True)
- Auto-generated fields: `login`, `id`
- Fields that cannot be set during initialization

### Dataclass Features
```python
@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)  # Cannot set during __init__
    id: str = field(init=False)
    
    def __post_init__(self):
        # Generate login and id after initialization
```

### Key Dataclass Concepts
- `@dataclass` decorator auto-generates methods
- `field(init=False)` prevents initialization of certain fields
- `__post_init__()` runs after `__init__()` for custom logic
- `field(default_factory=function)` for dynamic defaults

### Learning Points
- Modern Python class syntax
- Separation of user input from computed values
- Automatic ID generation patterns

---

## 🔧 General Best Practices

### Code Structure Requirements
```python
def main():
    # Your tests and error handling
    # All code logic goes here

if __name__ == "__main__":
    main()
```

**Why?** This pattern:
- Prevents code execution on import
- Makes code reusable as a module
- Clearly separates test code from implementation

### Import Standards
```python
# ✅ Good - Explicit
import numpy as np
from dataclasses import dataclass

# ❌ Bad - Wildcard imports forbidden
from pandas import *
```

### Documentation Requirements
Every function, class, and method needs a docstring:
```python
def calculate_mean(values: list) -> float:
    """
    Calculate the arithmetic mean of a list of numbers.
    
    Args:
        values: List of numeric values
    
    Returns:
        The mean as a float
    """
    return sum(values) / len(values)
```

---

## 🚨 Common Pitfalls to Avoid

1. **Global Variables**: Never use them. Pass data through function parameters.
2. **Uncaught Exceptions**: Always handle errors gracefully
3. **Global Scope Code**: All logic must be inside functions
4. **Using `global` keyword**: Forbidden. Use function parameters and return values
5. **Missing docstrings**: Every callable needs documentation

---

## 📊 Statistical Formulas Reference

For Exercise 00, you'll need:

- **Mean**: `sum(values) / count`
- **Median**: Middle value when sorted (or average of two middle values)
- **Quartile 25%**: Value at 25th percentile
- **Quartile 75%**: Value at 75th percentile
- **Variance**: Average of squared differences from mean
- **Standard Deviation**: Square root of variance

---

## 💡 Tips for Success

1. **Start Simple**: Get basic functionality working before handling edge cases
2. **Test Incrementally**: Test each function as you write it
3. **Read Error Messages**: Python's error messages are helpful - read them carefully
4. **Use Type Hints**: They help catch bugs early and make code more readable
5. **Follow the Prototypes**: The exact function signatures are provided - use them

---

## 🎓 Why This Matters

These exercises teach patterns you'll use constantly in data science:

- **Variable args**: Essential for flexible APIs (think `pandas.concat()`, `numpy.stack()`)
- **Closures**: Used in callbacks, event handlers, and state management
- **Decorators**: Critical for logging, timing, caching (`@lru_cache`, `@property`)
- **Dataclasses**: Modern way to define data structures in pipelines

Clean code isn't just academic - it's what separates a functioning script from maintainable, production-ready data science code.

---

## 📝 Submission Checklist

- [ ] All files in correct directories (ex00/, ex01/, ex02/, ex03/)
- [ ] Correct filenames (statistics.py, in_out.py, callLimit.py, new_student.py)
- [ ] Python 3.10 compatible
- [ ] No code in global scope
- [ ] All functions have docstrings
- [ ] Code passes flake8 linting
- [ ] All exceptions properly caught
- [ ] No global variables or `global` keyword usage
- [ ] Explicit imports only

**Good luck, and may your code be clean! 🚀**