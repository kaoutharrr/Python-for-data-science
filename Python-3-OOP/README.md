# Object-Oriented Programming in Python - Educational Guide

## Overview

This guide covers essential Object-Oriented Programming (OOP) concepts in Python, focusing on classes, inheritance, abstract classes, method overloading, decorators, and the diamond problem. These exercises are designed to help data scientists write better, more maintainable code.

---

## Table of Contents

1. [Why OOP Matters for Data Scientists](#why-oop-matters)
2. [Abstract Classes and Methods](#abstract-classes)
3. [Class Inheritance](#inheritance)
4. [Special Methods (Dunder Methods)](#dunder-methods)
5. [Class Methods and Decorators](#decorators)
6. [Properties (Getters and Setters)](#properties)
7. [The Diamond Problem](#diamond-problem)
8. [Operator Overloading](#operator-overloading)
9. [Static Methods](#static-methods)
10. [Best Practices](#best-practices)

---

## <a name="why-oop-matters"></a>1. Why OOP Matters for Data Scientists

Data scientists often write "shitcode" (inefficient, hard-to-maintain code) because they:
- Use too many hard-coded variables
- Write scripts instead of reusable modules
- Neglect proper code structure
- Focus on quick results over maintainability

**OOP helps by:**
- Organizing code into logical, reusable structures
- Encapsulating data and behavior together
- Making code easier to test, debug, and extend
- Promoting code reuse through inheritance
- Creating clear interfaces between different parts of your program

---

## <a name="abstract-classes"></a>2. Abstract Classes and Methods

### What is an Abstract Class?

An **abstract class** is a blueprint that cannot be instantiated directly. It's designed to be inherited by other classes and typically contains one or more abstract methods that must be implemented by child classes.

### Why Use Abstract Classes?

- **Enforce structure**: Ensure all child classes implement specific methods
- **Define interfaces**: Create a contract that subclasses must follow
- **Prevent instantiation**: Stop creation of incomplete or generic objects
- **Documentation**: Make code intent clear to other developers

### Key Components

```python
from abc import ABC, abstractmethod
```

- `ABC`: Abstract Base Class - the parent class for all abstract classes
- `@abstractmethod`: Decorator that marks a method as abstract (must be overridden)

### Exercise 00 Context

Create a `Character` abstract class that:
- Cannot be instantiated directly
- Has a `first_name` attribute
- Has an `is_alive` attribute (default: True)
- Has an abstract method to change the character's state

The `Stark` class inherits from `Character` and provides a concrete implementation.

### Key Concepts

**Abstract Method**: A method declared in an abstract class but contains no implementation. Subclasses MUST implement it.

**Concrete Class**: A class that provides implementations for all abstract methods and can be instantiated.

---

## <a name="inheritance"></a>3. Class Inheritance

### What is Inheritance?

Inheritance allows a class (child/subclass) to acquire attributes and methods from another class (parent/superclass). This promotes code reuse and establishes relationships between classes.

### Types of Inheritance

1. **Single Inheritance**: One child, one parent
2. **Multiple Inheritance**: One child, multiple parents
3. **Multilevel Inheritance**: Child becomes parent to another class
4. **Hierarchical Inheritance**: Multiple children from one parent

### Exercise 01 Context

Create `Baratheon` and `Lannister` families that:
- Inherit from the `Character` class
- Add family-specific attributes (family_name, eyes, hairs)
- Can be instantiated directly (not abstract)

### The `super()` Function

`super()` allows you to call methods from the parent class. This is essential for:
- Calling parent constructors
- Extending parent functionality without replacing it
- Maintaining the inheritance chain

### Method Resolution Order (MRO)

Python uses C3 linearization to determine the order in which base classes are searched when looking for a method. You can view it with `ClassName.__mro__` or `ClassName.mro()`.

---

## <a name="dunder-methods"></a>4. Special Methods (Dunder Methods)

### What are Dunder Methods?

Dunder methods (double underscore methods, like `__init__`, `__str__`) are special methods that Python calls automatically in certain situations. They allow your classes to integrate with Python's built-in operations.

### Common Dunder Methods

**`__init__(self, ...)`**
- Constructor method
- Called when creating a new instance
- Used to initialize attributes

**`__str__(self)`**
- Returns a human-readable string representation
- Called by `str()` and `print()`
- Should return something user-friendly

**`__repr__(self)`**
- Returns an unambiguous string representation
- Called by `repr()` and in the interactive shell
- Should ideally return a string that could recreate the object
- Fallback if `__str__` is not defined

**`__dict__`**
- Not a method, but an attribute
- Contains all instance attributes as a dictionary
- Useful for debugging and introspection

### Exercise 01 Context

Implement `__str__` and `__repr__` to return meaningful string representations of family members rather than default object representations.

---

## <a name="decorators"></a>5. Class Methods and Decorators

### What is a Decorator?

A decorator is a function that modifies or enhances another function or method. It's denoted with the `@` symbol.

### Common Class Decorators

**`@classmethod`**
- Receives the class (cls) as the first argument instead of instance (self)
- Can create alternative constructors
- Can access and modify class state
- Cannot access instance-specific data

**`@staticmethod`**
- Doesn't receive self or cls automatically
- Behaves like a regular function but belongs to the class namespace
- Used for utility functions related to the class

**`@abstractmethod`**
- Marks a method as abstract
- Must be implemented by concrete subclasses
- Part of the ABC module

**`@property`**
- Makes a method accessible like an attribute
- Used for getters, setters, and deleters

### Exercise 01 Context

Create a `create_lannister` class method that acts as an alternative constructor, allowing you to create Lannister characters in a different way (factory pattern).

---

## <a name="properties"></a>6. Properties (Getters and Setters)

### What are Properties?

Properties allow you to add logic to attribute access while maintaining a simple attribute-like interface. They're Python's way of implementing getters and setters.

### Why Use Properties?

- **Validation**: Check values before setting them
- **Computed attributes**: Calculate values on-the-fly
- **Encapsulation**: Hide internal representation
- **Backward compatibility**: Add logic later without changing the interface
- **Read-only attributes**: Prevent modification

### Property Decorators

**`@property`** - Defines the getter method
**`@attribute.setter`** - Defines the setter method
**`@attribute.deleter`** - Defines the deleter method

### Exercise 02 Context

The `King` class uses properties to control access to physical characteristics (eyes, hairs). This demonstrates:
- Encapsulation: Internal state is protected
- Controlled mutation: Changes go through validation
- Clean interface: Users call simple methods like `set_eyes()` and `get_eyes()`

---

## <a name="diamond-problem"></a>7. The Diamond Problem

### What is the Diamond Problem?

The diamond problem occurs in multiple inheritance when a class inherits from two classes that share a common ancestor. This creates ambiguity: which parent's method should be called?

```
    Character
      /   \
Baratheon Lannister
      \   /
       King
```

### Exercise 02 Context

`King` inherits from both `Baratheon` and `Lannister`, which both inherit from `Character`. This is the diamond pattern.

### Python's Solution: C3 Linearization

Since Python 2.3, Python uses C3 linearization (also called C3 superclass linearization or MRO) to solve this problem. It creates a consistent, predictable order for method lookup.

**Key Rules:**
1. Children are checked before parents
2. Parents are checked in the order they're listed
3. A class only appears once in the MRO
4. The order preserves the monotonicity (local precedence order)

### Checking MRO

You can inspect the Method Resolution Order:
```python
print(King.__mro__)
print(King.mro())
```

### Practical Implications

- First parent's attributes take precedence
- Use `super()` to ensure all parent constructors are called
- Be explicit about which parent's method you want when needed
- Document the inheritance structure clearly

---

## <a name="operator-overloading"></a>8. Operator Overloading

### What is Operator Overloading?

Operator overloading allows you to define custom behavior for built-in operators (+, -, *, /) when used with your custom objects.

### Common Operator Methods

**Arithmetic Operators:**
- `__add__(self, other)` - Addition (+)
- `__sub__(self, other)` - Subtraction (-)
- `__mul__(self, other)` - Multiplication (*)
- `__truediv__(self, other)` - Division (/)
- `__floordiv__(self, other)` - Floor division (//)
- `__mod__(self, other)` - Modulo (%)
- `__pow__(self, other)` - Power (**)

**Comparison Operators:**
- `__eq__(self, other)` - Equal (==)
- `__ne__(self, other)` - Not equal (!=)
- `__lt__(self, other)` - Less than (<)
- `__le__(self, other)` - Less than or equal (<=)
- `__gt__(self, other)` - Greater than (>)
- `__ge__(self, other)` - Greater than or equal (>=)

### Exercise 03 Context

Create a calculator class that performs vector-scalar operations:
- Addition: Add a scalar to each vector element
- Multiplication: Multiply each vector element by a scalar
- Subtraction: Subtract a scalar from each vector element
- Division: Divide each vector element by a scalar

**Key Point:** These methods modify the object in place and return `None`, not a new object. This is indicated by the `-> None` return type annotation.

### Design Considerations

- Should operations create new objects or modify existing ones?
- What should happen with invalid operations?
- How should different types interact?
- What should the method return?

---

## <a name="static-methods"></a>9. Static Methods

### What are Static Methods?

Static methods are methods that belong to a class but don't require access to instance (self) or class (cls) data. They're like regular functions but are namespaced within the class.

### When to Use Static Methods

- Utility functions related to the class
- Functions that don't need instance or class state
- Logical grouping of related functions
- Alternative to module-level functions when they're closely tied to a class

### Exercise 04 Context

Create a calculator class with static methods that perform vector operations:
- `dotproduct`: Calculate dot product of two vectors
- `add_vec`: Add two vectors element-wise
- `sous_vec`: Subtract two vectors element-wise

**Key Feature:** These methods can be called without creating an instance:
```python
calculator.dotproduct(a, b)  # No need for: calc = calculator()
```

### Static Methods vs Class Methods

| Static Method | Class Method |
|---------------|--------------|
| No automatic first parameter | Receives cls as first parameter |
| Cannot access instance/class state | Can access/modify class state |
| Pure utility function | Can create instances |
| Use `@staticmethod` | Use `@classmethod` |

---

## <a name="best-practices"></a>10. Best Practices

### Code Organization

1. **No global scope code**: Always use functions and classes
2. **Main guard**: Use `if __name__ == "__main__":` pattern
3. **Error handling**: Catch and handle exceptions appropriately
4. **Documentation**: Every class and method needs a docstring

### OOP Principles

**SOLID Principles:**
- **S**ingle Responsibility: One class, one purpose
- **O**pen/Closed: Open for extension, closed for modification
- **L**iskov Substitution: Subclasses should be substitutable for parent classes
- **I**nterface Segregation: Many specific interfaces better than one general
- **D**ependency Inversion: Depend on abstractions, not concretions

### Python-Specific Guidelines

1. **Use explicit imports**: `import numpy as np` not `from pandas import *`
2. **Follow PEP 8**: Use flake8 for style checking
3. **Type hints**: Add type annotations for clarity
4. **Composition over inheritance**: Don't inherit just to reuse code
5. **Keep it simple**: Don't over-engineer

### Documentation Standards

Every class and method should have a docstring that explains:
- What it does
- Parameters and their types
- Return value and type
- Any exceptions that might be raised
- Usage examples (for complex functionality)

### Testing Recommendations

- Write test functions for your classes
- Test edge cases and error conditions
- Use meaningful variable names in tests
- Test inheritance hierarchies thoroughly
- Verify that abstract classes cannot be instantiated

---

## Key Takeaways

1. **Abstract classes** enforce structure and prevent instantiation of incomplete classes
2. **Inheritance** promotes code reuse but should be used judiciously
3. **Dunder methods** integrate your classes with Python's built-in operations
4. **Properties** provide controlled access to attributes with validation
5. **The diamond problem** is solved by C3 linearization in Python
6. **Operator overloading** makes custom objects behave like built-in types
7. **Class methods** provide alternative constructors and class-level operations
8. **Static methods** are utility functions that belong to a class namespace
9. **Good OOP** leads to maintainable, testable, and reusable code
10. **Documentation** is not optional - it's essential for understanding and maintaining code

---

## Further Learning

To deepen your OOP knowledge:
- Study design patterns (Factory, Singleton, Observer, etc.)
- Learn about metaclasses for advanced class customization
- Explore dataclasses for simpler class definitions
- Investigate Protocol classes for structural typing
- Practice refactoring procedural code to OOP
- Read "Design Patterns" by Gang of Four
- Explore Python's data model in the official documentation

Remember: The goal isn't to use every OOP feature in every project, but to know when each tool is appropriate. Good design comes from experience and understanding trade-offs.