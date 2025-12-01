# 🐍 Python Piscine - Day 0: Complete Educational Guide

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Educational-green?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Difficulty-Beginner-brightgreen?style=for-the-badge)

**Master Python Fundamentals Through Hands-On Practice**

[Introduction](#-introduction) • [Concepts](#-core-concepts) • [Exercises](#-exercises-overview) • [Resources](#-resources)

</div>

---

## 📋 Table of Contents

- [Introduction](#-introduction)
- [Core Concepts](#-core-concepts)
  - [Data Types](#1-data-types-in-python)
  - [Functions](#2-functions-and-docstrings)
  - [Modules and Imports](#3-modules-and-imports)
  - [Command-Line Arguments](#4-command-line-arguments)
  - [Type Checking](#5-type-checking-and-introspection)
- [Exercises Overview](#-exercises-overview)
- [Best Practices](#-best-practices)
- [Visual Reference](#-visual-reference)
- [Resources](#-resources)

---

## 🎯 Introduction

This project introduces you to **Python fundamentals** through 10 progressive exercises. You'll learn the building blocks needed for data science: data structures, functions, string manipulation, and package management.

### Prerequisites

```bash
✅ Python 3.10 installed
✅ Git configured
✅ Text editor/IDE ready
✅ Terminal knowledge
```

### Project Structure

```
ex00/  → Basic data types manipulation
ex01/  → Working with date/time libraries
ex02/  → Creating your first function
ex03/  → Understanding "null" values
ex04/  → Command-line arguments
ex05/  → String analysis program
ex06/  → List comprehensions & lambda
ex07/  → Dictionaries (Morse code)
ex08/  → Generators and yield
ex09/  → Creating a Python package
```

---

## 🧠 Core Concepts

### 1. Data Types in Python

Python has several built-in data structures, each with unique characteristics:

#### 📦 **Lists** - Ordered & Mutable

```
┌─────────────────────────────┐
│  Lists: [1, 2, 3, "hello"]  │
├─────────────────────────────┤
│ ✓ Ordered (index-based)     │
│ ✓ Mutable (can change)      │
│ ✓ Allows duplicates         │
│ ✓ Access: list[0]           │
└─────────────────────────────┘
```

**Visual Representation:**
```
Index:  0    1    2    3
       ┌────┬────┬────┬────┐
List:  │ 1  │ 2  │ 3  │ 4  │  ← Can modify any element
       └────┴────┴────┴────┘
```

#### 📌 **Tuples** - Ordered & Immutable

```
┌─────────────────────────────┐
│ Tuples: (1, 2, 3, "hello")  │
├─────────────────────────────┤
│ ✓ Ordered (index-based)     │
│ ✗ Immutable (can't change)  │
│ ✓ Allows duplicates         │
│ ✓ Access: tuple[0]          │
└─────────────────────────────┘
```

**Visual Representation:**
```
Index:   0    1    2    3
        ┌────┬────┬────┬────┐
Tuple:  │ 1  │ 2  │ 3  │ 4  │  ← LOCKED! Cannot modify
        └────┴────┴────┴────┘
         🔒   🔒   🔒   🔒
```

#### 🎲 **Sets** - Unordered & Unique

```
┌─────────────────────────────┐
│   Sets: {1, 2, 3, 4}        │
├─────────────────────────────┤
│ ✗ Unordered (no index)      │
│ ✓ Mutable (can change)      │
│ ✗ No duplicates             │
│ ✓ Fast membership testing   │
└─────────────────────────────┘
```

**Visual Representation:**
```
     {1, 2, 3, 3, 4}
          ↓
    Automatically removes duplicates
          ↓
       {1, 2, 3, 4}
```

#### 🗂️ **Dictionaries** - Key-Value Pairs

```
┌─────────────────────────────┐
│ Dict: {"name": "John"}      │
├─────────────────────────────┤
│ ✗ Unordered (key-based)     │
│ ✓ Mutable (can change)      │
│ ✓ Unique keys               │
│ ✓ Access: dict["key"]       │
└─────────────────────────────┘
```

**Visual Representation:**
```
┌──────────┬──────────┐
│   Key    │  Value   │
├──────────┼──────────┤
│ "name"   │ "John"   │
│ "age"    │   30     │
│ "city"   │ "Paris"  │
└──────────┴──────────┘
```

#### 📝 **Strings** - Immutable Sequences

```
┌─────────────────────────────┐
│ String: "Hello, World!"     │
├─────────────────────────────┤
│ ✓ Ordered (index-based)     │
│ ✗ Immutable (can't change)  │
│ ✓ Iterable                  │
│ ✓ Many built-in methods     │
└─────────────────────────────┘
```

---

### 2. Functions and Docstrings

Functions are reusable blocks of code that perform specific tasks.

#### Function Anatomy

```
┌─────────────────────────────────────────┐
│  def function_name(param: type) -> int: │  ← Function signature
│      """                                │
│      This is a docstring.               │  ← Documentation
│      It explains what the function does.│
│      """                                │
│      # Function body                    │  ← Implementation
│      result = param + 1                 │
│      return result                      │  ← Return value
└─────────────────────────────────────────┘
```

#### Type Annotations

```
Function Input        Return Type
      ↓                   ↓
def greet(name: str) -> str:
              ↑
         Type hint
```

**Benefits:**
- 📖 Better code documentation
- 🐛 Easier debugging
- 🔍 IDE autocomplete support
- ✅ Type checking tools

---

### 3. Modules and Imports

Modules are Python files containing functions, classes, and variables that you can reuse.

#### Import Visualization

```
┌──────────────────────────────────────┐
│  Your Script: main.py                │
│                                      │
│  import time                         │ ← Import entire module
│  from datetime import datetime       │ ← Import specific item
│  import numpy as np                  │ ← Import with alias
│                                      │
│  time.sleep(1)          ✓ Allowed   │
│  datetime.now()         ✓ Allowed   │
│  np.array([1,2,3])      ✓ Allowed   │
│                                      │
│  from pandas import *   ✗ FORBIDDEN │
└──────────────────────────────────────┘
```

#### Common Standard Library Modules

```
┌────────────┬──────────────────────────────┐
│  Module    │  Purpose                     │
├────────────┼──────────────────────────────┤
│  sys       │  System-specific parameters  │
│  time      │  Time-related functions      │
│  datetime  │  Date and time manipulation  │
│  os        │  Operating system interface  │
│  math      │  Mathematical functions      │
└────────────┴──────────────────────────────┘
```

---

### 4. Command-Line Arguments

Command-line arguments allow users to pass data to your program when running it.

#### How sys.argv Works

```
Terminal Command:
$ python script.py arg1 arg2 arg3

sys.argv representation:
┌───────────┬────────┬────────┬────────┐
│ Index: 0  │   1    │   2    │   3    │
├───────────┼────────┼────────┼────────┤
│script.py  │ arg1   │ arg2   │ arg3   │
└───────────┴────────┴────────┴────────┘
     ↑          ↑        ↑        ↑
  Script    First    Second   Third
   name     argument argument argument
```

**Important Notes:**
- `sys.argv[0]` is always the script name
- `sys.argv[1:]` gives you all arguments (excluding script name)
- All arguments are strings by default
- `len(sys.argv)` tells you total number of items

---

### 5. Type Checking and Introspection

Python provides tools to inspect objects at runtime.

#### The type() Function

```
┌──────────────────────────────────┐
│  type(object) → Returns class    │
└──────────────────────────────────┘

Examples:
type(42)           → <class 'int'>
type("hello")      → <class 'str'>
type([1, 2, 3])    → <class 'list'>
type({"a": 1})     → <class 'dict'>
```

#### "Null" Values in Python

```
┌────────────┬─────────────┬──────────────────┐
│   Value    │    Type     │   Description    │
├────────────┼─────────────┼──────────────────┤
│   None     │  NoneType   │  True null       │
│ float("NaN")│   float    │  Not a Number    │
│     0      │    int      │  Zero integer    │
│    ""      │    str      │  Empty string    │
│   False    │    bool     │  Boolean false   │
└────────────┴─────────────┴──────────────────┘
```

**Comparison Operators:**
```
== (equality)    →  Compares values
is (identity)    →  Compares object identity

None check:      use "is None"  ✓
Boolean check:   use "is False" ✓
Value check:     use "== 0"     ✓
```

---

## 📚 Exercises Overview

### Exercise 00: First Python Script
**Concepts:** Data type manipulation, mutability
```
┌─────────────────────────────┐
│ Input: Built-in structures  │
│ Task: Modify to show greets │
│ Learn: Mutability concepts  │
└─────────────────────────────┘
```

### Exercise 01: Date & Time Formatting
**Concepts:** Modules, string formatting, timestamps
```
┌──────────────────────────────┐
│ Input: Current time          │
│ Task: Format in multiple ways│
│ Learn: time, datetime modules│
└──────────────────────────────┘
```

### Exercise 02: Type Identifier Function
**Concepts:** Functions, type checking, returns
```
┌─────────────────────────────┐
│ Input: Any object           │
│ Task: Print type, return 42 │
│ Learn: type(), conditionals │
└─────────────────────────────┘
```

### Exercise 03: NULL Detection
**Concepts:** Falsy values, NaN, type hierarchy
```
┌─────────────────────────────┐
│ Input: Various "null" values│
│ Task: Identify and print    │
│ Learn: None, NaN, falsiness │
└─────────────────────────────┘
```

### Exercise 04: Even/Odd Checker
**Concepts:** sys.argv, assertions, modulo
```
┌─────────────────────────────┐
│ Input: Command-line number  │
│ Task: Check if even/odd     │
│ Learn: CLI args, validation │
└─────────────────────────────┘
```

### Exercise 05: String Analyzer
**Concepts:** String methods, character classification
```
┌─────────────────────────────┐
│ Input: Text string          │
│ Task: Count char types      │
│ Learn: str methods, loops   │
└─────────────────────────────┘
```

### Exercise 06: Custom Filter Function
**Concepts:** List comprehensions, lambda, filter
```
┌─────────────────────────────┐
│ Input: String + number      │
│ Task: Filter words by length│
│ Learn: Comprehensions, λ    │
└─────────────────────────────┘
```

### Exercise 07: Morse Code Encoder
**Concepts:** Dictionaries, string manipulation
```
┌─────────────────────────────┐
│ Input: Alphanumeric text    │
│ Task: Convert to Morse      │
│ Learn: Dict lookup, loops   │
└─────────────────────────────┘
```

### Exercise 08: Loading Bar
**Concepts:** Generators, yield, terminal control
```
┌─────────────────────────────┐
│ Input: Range iterator       │
│ Task: Create progress bar   │
│ Learn: Generators, yield    │
└─────────────────────────────┘
```

### Exercise 09: Package Creation
**Concepts:** Package structure, pip, distribution
```
┌─────────────────────────────┐
│ Input: Python functions     │
│ Task: Create installable pkg│
│ Learn: setup.py, packaging  │
└─────────────────────────────┘
```

---

## ✨ Best Practices

### Code Organization

```python
# ✓ GOOD: Clear structure
"""Module docstring explaining purpose."""

import sys
from datetime import datetime


def main():
    """Main function with clear flow."""
    # Implementation here
    pass


if __name__ == "__main__":
    main()
```

```python
# ✗ BAD: Global scope code
import sys

x = 10  # Global variable - FORBIDDEN
print("Running...")  # Code in global scope

def main():
    pass
```

### Naming Conventions

```
┌──────────────────┬────────────────┬─────────────┐
│   Type           │   Convention   │   Example   │
├──────────────────┼────────────────┼─────────────┤
│ Variables        │  snake_case    │  user_name  │
│ Functions        │  snake_case    │  get_data() │
│ Classes          │  PascalCase    │  UserModel  │
│ Constants        │  UPPER_CASE    │  MAX_SIZE   │
│ Private          │  _leading      │  _internal  │
└──────────────────┴────────────────┴─────────────┘
```

### Flake8 Linting

```bash
# Install
$ pip install flake8

# Run on file
$ flake8 your_script.py

# Common issues caught:
• Line too long (>79 characters)
• Unused imports
• Missing whitespace
• Undefined variables
```

---

## 🎨 Visual Reference

### Python Data Type Hierarchy

```
                    object
                      │
      ┌───────────────┼───────────────┐
      │               │               │
   Sequence        Mapping          Set
      │               │               │
  ┌───┴───┐          dict          set
  │       │                       frozenset
 str    list
       tuple
```

### String Formatting Evolution

```
Old Style (%)
"Hello %s, you are %d years old" % (name, age)
             ↓
.format() Method
"Hello {}, you are {} years old".format(name, age)
             ↓
F-Strings (Python 3.6+) ← USE THIS
f"Hello {name}, you are {age} years old"
```

### List Comprehension vs Loop

```
Traditional Loop:
result = []
for item in range(10):
    if item % 2 == 0:
        result.append(item)

           ↓ TRANSFORM TO ↓

List Comprehension:
result = [item for item in range(10) if item % 2 == 0]

[expression for item in iterable if condition]
     ↑           ↑         ↑            ↑
  Output      Loop     Source      Filter
```

### Lambda Functions

```
Regular Function:
def add(x, y):
    return x + y

           ↓ EQUIVALENT TO ↓

Lambda Function:
add = lambda x, y: x + y

lambda parameters: expression
   ↑       ↑          ↑
Keyword  Input     Output
```

---

## 📖 Resources

### Official Documentation
- [Python 3.10 Documentation](https://docs.python.org/3.10/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Python Package Index (PyPI)](https://pypi.org/)

### Useful Tools
```bash
# Interactive Python
$ python3.10

# Package management
$ pip install <package>
$ pip list
$ pip show <package>

# Code formatting
$ flake8 <file>
```

### Key Python Built-in Functions

```
┌─────────────┬──────────────────────────────┐
│  Function   │  Purpose                     │
├─────────────┼──────────────────────────────┤
│  type()     │  Get object type             │
│  len()      │  Get length                  │
│  print()    │  Output to console           │
│  input()    │  Get user input              │
│  range()    │  Generate number sequence    │
│  enumerate()│  Get index + value in loop   │
│  zip()      │  Combine iterables           │
│  filter()   │  Filter items by condition   │
│  map()      │  Apply function to items     │
└─────────────┴──────────────────────────────┘
```

---

## 🎓 Learning Tips

1. **Read Error Messages** - Python error messages are descriptive
2. **Use the REPL** - Test small code snippets interactively
3. **Read Documentation** - The `__doc__` attribute is your friend
4. **Test Incrementally** - Don't write everything at once
5. **Use Version Control** - Commit often with clear messages

---

<div align="center">

### 🚀 Ready to Start Coding!

**Remember:** The goal is understanding, not just completion.

Made with ❤️ for Python learners

</div>