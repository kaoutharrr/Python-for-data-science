# 🎨 Python Piscine - Day 1: Array & Image Manipulation

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![NumPy](https://img.shields.io/badge/NumPy-Arrays-013243?style=for-the-badge&logo=numpy)
![PIL](https://img.shields.io/badge/Pillow-Images-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Educational-green?style=for-the-badge)

**Master Arrays, NumPy, and Image Processing**

[Introduction](#-introduction) • [Core Concepts](#-core-concepts) • [Exercises](#-exercises-overview) • [Image Processing](#-image-processing-fundamentals)

</div>

---

## 📋 Table of Contents

- [Introduction](#-introduction)
- [Core Concepts](#-core-concepts)
  - [Arrays vs Lists](#1-arrays-vs-lists)
  - [NumPy Arrays](#2-numpy-arrays)
  - [Image Representation](#3-image-representation-in-python)
  - [Array Slicing](#4-array-slicing)
  - [Array Operations](#5-array-operations)
- [Exercises Overview](#-exercises-overview)
- [Image Processing Fundamentals](#-image-processing-fundamentals)
- [Visual Reference](#-visual-reference)
- [Resources](#-resources)

---

## 🎯 Introduction

Day 1 focuses on **arrays and image manipulation**. You'll learn how computers store and manipulate images as arrays of numbers, and master essential NumPy operations for data science.

### What You'll Learn

```
✓ Array manipulation with NumPy
✓ Image loading and processing
✓ Color channels (RGB)
✓ Array slicing and indexing
✓ Image transformations
✓ Color filters
```

### Project Structure

```
ex00/  → BMI calculations with arrays
ex01/  → 2D array slicing
ex02/  → Loading images as arrays
ex03/  → Zooming into images
ex04/  → Rotating images (transpose)
ex05/  → Color filters (invert, red, green, blue, grey)
```

---

## 🧠 Core Concepts

### 1. Arrays vs Lists

#### Python Lists
```
┌─────────────────────────────────────┐
│  Python Lists: [1, 2, 3, 4, 5]      │
├─────────────────────────────────────┤
│ ✓ Dynamic size                      │
│ ✓ Can mix types                     │
│ ✗ Slow for math operations          │
│ ✗ No vectorization                  │
└─────────────────────────────────────┘
```

**Memory Representation:**
```
List: [1, "hello", 3.14, True]
       ↓     ↓      ↓     ↓
    [ptr] [ptr]  [ptr]  [ptr]  → Pointers to different objects
```

#### NumPy Arrays
```
┌─────────────────────────────────────┐
│  NumPy Arrays: array([1, 2, 3, 4])  │
├─────────────────────────────────────┤
│ ✓ Fixed size (efficient)            │
│ ✓ Same type only                    │
│ ✓ Fast math operations               │
│ ✓ Vectorization support              │
└─────────────────────────────────────┘
```

**Memory Representation:**
```
Array: [1, 2, 3, 4, 5]
        ↓  ↓  ↓  ↓  ↓
      [1][2][3][4][5]  → Contiguous memory block
```

---

### 2. NumPy Arrays

NumPy is the foundation of scientific computing in Python.

#### Creating Arrays

```python
import numpy as np

# From lists
arr = np.array([1, 2, 3, 4])

# Shape tells you dimensions
arr.shape  # (4,) - 1D array with 4 elements
```

#### Array Dimensions Visualization

```
1D Array (Vector):
[1, 2, 3, 4, 5]
     ↓
Shape: (5,)


2D Array (Matrix):
[[1, 2, 3],
 [4, 5, 6]]
     ↓
Shape: (2, 3)  → 2 rows, 3 columns


3D Array (Tensor):
[[[1, 2],
  [3, 4]],
 
 [[5, 6],
  [7, 8]]]
     ↓
Shape: (2, 2, 2)  → 2 layers, 2 rows, 2 columns
```

#### Shape Anatomy

```
┌─────────────────────────────────┐
│   array.shape = (4, 3, 2)       │
│                  ↓  ↓  ↓        │
│              depth │  │         │
│              rows ─┘  │         │
│              columns ─┘         │
└─────────────────────────────────┘
```

---

### 3. Image Representation in Python

Images are just 3D arrays of numbers!

#### RGB Image Structure

```
Image Dimensions:
┌────────────────────────────────┐
│  Shape: (Height, Width, 3)     │
│            ↓       ↓     ↓     │
│         Rows   Columns  RGB    │
└────────────────────────────────┘

Example: (256, 512, 3)
         ↓     ↓    ↓
    256 pixels high
    512 pixels wide
    3 color channels (R, G, B)
```

#### Color Channels

```
      Original Image (RGB)
              ↓
    ┌─────────┴─────────┐
    ↓         ↓         ↓
   Red     Green     Blue
 Channel  Channel  Channel

Each pixel has 3 values:
┌───┬───┬───┐
│ R │ G │ B │  Values: 0-255
└───┴───┴───┘

Example:
[255, 0, 0]    → Pure Red
[0, 255, 0]    → Pure Green
[0, 0, 255]    → Pure Blue
[255, 255, 0]  → Yellow
[0, 0, 0]      → Black
[255, 255, 255]→ White
```

#### Pixel Grid Visualization

```
Image as 2D Grid (simplified 4x4):

     Column 0   Column 1   Column 2   Column 3
    ┌──────────┬──────────┬──────────┬──────────┐
R 0 │ [R,G,B]  │ [R,G,B]  │ [R,G,B]  │ [R,G,B]  │
o   ├──────────┼──────────┼──────────┼──────────┤
w 1 │ [R,G,B]  │ [R,G,B]  │ [R,G,B]  │ [R,G,B]  │
    ├──────────┼──────────┼──────────┼──────────┤
  2 │ [R,G,B]  │ [R,G,B]  │ [R,G,B]  │ [R,G,B]  │
    ├──────────┼──────────┼──────────┼──────────┤
  3 │ [R,G,B]  │ [R,G,B]  │ [R,G,B]  │ [R,G,B]  │
    └──────────┴──────────┴──────────┴──────────┘

Each cell contains 3 numbers (RGB values)
```

---

### 4. Array Slicing

Slicing extracts portions of arrays without copying data.

#### 1D Array Slicing

```
Array:  [10, 20, 30, 40, 50, 60, 70]
Index:   0   1   2   3   4   5   6

arr[start:end:step]
     ↓     ↓    ↓
   Begin  Stop  Jump

Examples:
arr[1:4]    → [20, 30, 40]     (index 1 to 3)
arr[:3]     → [10, 20, 30]     (start to index 2)
arr[3:]     → [40, 50, 60, 70] (index 3 to end)
arr[::2]    → [10, 30, 50, 70] (every 2nd element)
arr[-2:]    → [60, 70]         (last 2 elements)
```

#### 2D Array Slicing

```
Original Array (4x3):
[[10, 20, 30],
 [40, 50, 60],
 [70, 80, 90],
 [11, 22, 33]]

arr[row_start:row_end, col_start:col_end]
        ↓                    ↓
    Row slice           Column slice


Examples:

arr[0:2, :]     → First 2 rows, all columns
[[10, 20, 30],
 [40, 50, 60]]

arr[:, 1:3]     → All rows, columns 1-2
[[20, 30],
 [50, 60],
 [80, 90],
 [22, 33]]

arr[1:-1, 1:2]  → Middle rows, column 1
[[50],
 [80]]
```

#### Negative Indexing

```
Array:  [10, 20, 30, 40, 50]
Index:   0   1   2   3   4
         ↓   ↓   ↓   ↓   ↓
Index:  -5  -4  -3  -2  -1

arr[-1]   → 50  (last element)
arr[-2]   → 40  (second to last)
arr[:-2]  → [10, 20, 30]  (all except last 2)
```

---

### 5. Array Operations

NumPy allows vectorized operations on entire arrays.

#### Element-wise Operations

```
Array 1: [1, 2, 3, 4]
Array 2: [5, 6, 7, 8]

Addition:
[1, 2, 3, 4] + [5, 6, 7, 8] = [6, 8, 10, 12]
 ↓   ↓   ↓   ↓
1+5 2+6 3+7 4+8

Multiplication:
[1, 2, 3, 4] * [5, 6, 7, 8] = [5, 12, 21, 32]
 ↓   ↓   ↓   ↓
1*5 2*6 3*7 4*8
```

#### Broadcasting

```
Broadcasting allows operations between arrays of different shapes:

Array:    [[1, 2, 3],      Scalar: 10
           [4, 5, 6]]

Array + 10:
[[1+10, 2+10, 3+10],
 [4+10, 5+10, 6+10]]

Result:
[[11, 12, 13],
 [14, 15, 16]]
```

---

## 📚 Exercises Overview

### Exercise 00: Give my BMI
**Concepts:** Array operations, BMI calculation, error handling

```
┌────────────────────────────────────┐
│ Input: height[], weight[]          │
│ Task: Calculate BMI for each       │
│ Formula: BMI = weight / height²    │
│ Learn: Vectorized operations       │
└────────────────────────────────────┘

Visual:
height = [2.71, 1.15]
weight = [165.3, 38.4]
           ↓
BMI[i] = weight[i] / (height[i] ** 2)
           ↓
[22.50, 29.03]
```

### Exercise 01: 2D Array Slicing
**Concepts:** Array shape, slicing, 2D arrays

```
┌────────────────────────────────────┐
│ Input: 2D array, start, end        │
│ Task: Slice rows from start to end │
│ Learn: Array slicing, shape        │
└────────────────────────────────────┘

Visual:
family = [[1.80, 78.4],    ← Row 0
          [2.15, 102.7],   ← Row 1
          [2.10, 98.5],    ← Row 2
          [1.88, 75.2]]    ← Row 3

slice_me(family, 0, 2)  → Rows 0-1
slice_me(family, 1, -2) → Row 1 only
```

### Exercise 02: Load my Image
**Concepts:** Image loading, JPG/JPEG format, RGB arrays

```
┌────────────────────────────────────┐
│ Input: Image file path             │
│ Task: Load and display as array    │
│ Learn: Image I/O, RGB structure    │
└────────────────────────────────────┘

Image File → Array Conversion:
┌──────────┐
│  Image   │
│  .jpg    │  → Load → [[R, G, B],
└──────────┘                [R, G, B],
                             [R, G, B]]
```

### Exercise 03: Zoom on me
**Concepts:** Array slicing, image cropping, grayscale conversion

```
┌────────────────────────────────────┐
│ Input: animal.jpeg                 │
│ Task: Crop and display zoomed area │
│ Learn: 3D array slicing, channels  │
└────────────────────────────────────┘

Visual Process:
Original (768, 1024, 3)
        ↓ Slice
Cropped (400, 400, 3)
        ↓ Convert to grayscale
Result  (400, 400, 1) or (400, 400)
```

### Exercise 04: Rotate me
**Concepts:** Transpose, matrix rotation, manual implementation

```
┌────────────────────────────────────┐
│ Input: Cropped image array         │
│ Task: Transpose (rotate 90°)       │
│ Learn: Matrix transpose algorithm  │
└────────────────────────────────────┘

Transpose Visualization:
Original:        Transposed:
[[1, 2, 3],      [[1, 4, 7],
 [4, 5, 6],  →    [2, 5, 8],
 [7, 8, 9]]       [3, 6, 9]]

Rows become columns!
```

### Exercise 05: Pimp my Image
**Concepts:** Color manipulation, filter algorithms, operator restrictions

```
┌────────────────────────────────────┐
│ Input: Image array                 │
│ Task: Apply 5 color filters        │
│ Learn: RGB manipulation, filters   │
└────────────────────────────────────┘

Filters Overview:
┌──────────┬─────────────────────────┐
│ Filter   │ Effect                  │
├──────────┼─────────────────────────┤
│ Invert   │ 255 - each RGB value    │
│ Red      │ Keep R, zero G and B    │
│ Green    │ Keep G, zero R and B    │
│ Blue     │ Keep B, zero R and G    │
│ Grey     │ Average RGB values      │
└──────────┴─────────────────────────┘
```

---

## 🎨 Image Processing Fundamentals

### RGB Color Model

```
         RGB Color Cube

          White (255,255,255)
               ╱│╲
              ╱ │ ╲
        Yellow │  Cyan
            ╱  │   ╲
           ╱   │    ╲
      Red ─────┼───── Green
          ╲    │    ╱
           ╲   │   ╱
        Magenta│  ╱
             ╲ │ ╱
              ╲│╱
          Black (0,0,0)
```

### Color Filter Operations

#### Invert Filter
```
Original Pixel: [100, 150, 200]
                     ↓
Invert: [255-100, 255-150, 255-200]
                     ↓
Result:         [155, 105, 55]

Visual Effect: Dark becomes light, light becomes dark
```

#### Red Filter
```
Original Pixel: [100, 150, 200]
                  ↓    ↓    ↓
Keep Red:       [100,  0,   0]

Visual Effect: Only red channel visible
```

#### Green Filter
```
Original Pixel: [100, 150, 200]
                  ↓    ↓    ↓
Keep Green:     [0,  150,   0]

Visual Effect: Only green channel visible
```

#### Blue Filter
```
Original Pixel: [100, 150, 200]
                  ↓    ↓    ↓
Keep Blue:      [0,    0,  200]

Visual Effect: Only blue channel visible
```

#### Greyscale Filter
```
Original Pixel: [100, 150, 200]
                     ↓
Average: (100 + 150 + 200) / 3 = 150
                     ↓
Result:         [150, 150, 150]

Visual Effect: Remove color, keep luminosity
```

---

## 🔧 Visual Reference

### Image Array Structure

```
3D Image Array Structure:

        Width (columns)
    ←─────────────────→
  ↑ ┌─────────────────┐  ┌─┐
  │ │                 │  │R│ ← Red channel
H │ │                 │  ├─┤
e │ │     Image       │  │G│ ← Green channel
i │ │                 │  ├─┤
g │ │                 │  │B│ ← Blue channel
h │ └─────────────────┘  └─┘
t │
  ↓

Access pattern:
image[row, col, channel]
  ↓     ↓      ↓
 y-axis x-axis RGB (0,1,2)
```

### BMI Calculation Visualization

```
Input Arrays:
heights = [h₁, h₂, h₃, ...]
weights = [w₁, w₂, w₃, ...]

Element-wise Calculation:
BMI[i] = weight[i] / (height[i])²

┌──────┬──────────┬──────────┐
│ i    │ Calc     │ Result   │
├──────┼──────────┼──────────┤
│ 0    │ w₁/h₁²   │ BMI₁     │
│ 1    │ w₂/h₂²   │ BMI₂     │
│ 2    │ w₃/h₃²   │ BMI₃     │
└──────┴──────────┴──────────┘
```

### Array Transpose Mechanics

```
Original Matrix (3x4):
     Col 0  Col 1  Col 2  Col 3
Row 0 [ a     b      c      d  ]
Row 1 [ e     f      g      h  ]
Row 2 [ i     j      k      l  ]

After Transpose (4x3):
     Col 0  Col 1  Col 2
Row 0 [ a     e      i  ]
Row 1 [ b     f      j  ]
Row 2 [ c     g      k  ]
Row 3 [ d     h      l  ]

Algorithm Concept:
transposed[j][i] = original[i][j]
```

### Image Slicing for Zoom

```
Original Image (1024 x 768):
┌─────────────────────────────┐
│                             │
│     ┌─────────────┐         │
│     │             │         │ ← Zoom area
│     │   Region    │         │   (400 x 400)
│     │   of        │         │
│     │   Interest  │         │
│     └─────────────┘         │
│                             │
└─────────────────────────────┘

Slice:
zoomed = img[y_start:y_end, x_start:x_end]
```

---

## 📖 Essential NumPy Operations

### Array Creation

```python
┌─────────────────────────────────────┐
│ import numpy as np                  │
│                                     │
│ # From list                         │
│ arr = np.array([1, 2, 3])          │
│                                     │
│ # Zeros                             │
│ zeros = np.zeros((3, 4))           │
│                                     │
│ # Ones                              │
│ ones = np.ones((2, 3))             │
│                                     │
│ # Range                             │
│ range_arr = np.arange(0, 10, 2)    │
└─────────────────────────────────────┘
```

### Array Properties

```
┌──────────────┬─────────────────────────┐
│  Property    │  Description            │
├──────────────┼─────────────────────────┤
│ .shape       │ Dimensions tuple        │
│ .ndim        │ Number of dimensions    │
│ .size        │ Total number of elements│
│ .dtype       │ Data type of elements   │
└──────────────┴─────────────────────────┘
```

### Common Image Libraries

```
┌──────────────┬─────────────────────────┐
│  Library     │  Use Case               │
├──────────────┼─────────────────────────┤
│ PIL/Pillow   │ Load/save images        │
│ NumPy        │ Array operations        │
│ Matplotlib   │ Display images          │
│ OpenCV       │ Advanced processing     │
└──────────────┴─────────────────────────┘
```

---

## 🎓 Key Concepts Summary

### Array Indexing Rules

```
┌─────────────────────────────────────┐
│ 1D: arr[index]                      │
│ 2D: arr[row, col]                   │
│ 3D: arr[depth, row, col]            │
│ RGB: img[height, width, channel]    │
└─────────────────────────────────────┘
```

### Slicing Syntax

```
array[start:stop:step]
  ↓      ↓     ↓
Begin  End   Jump
(incl) (excl)

Special values:
• Omit start  → from beginning
• Omit stop   → to end
• Negative    → count from end
• step = -1   → reverse
```

### Channel Conventions

```
┌──────────┬─────────┬──────────────┐
│ Channel  │  Index  │  Color       │
├──────────┼─────────┼──────────────┤
│    0     │  [:,:,0]│  Red         │
│    1     │  [:,:,1]│  Green       │
│    2     │  [:,:,2]│  Blue        │
└──────────┴─────────┴──────────────┘
```

---

## 💡 Best Practices

### Error Handling

```python
✓ GOOD: Check array shapes
if len(height) != len(weight):
    raise ValueError("Arrays must be same length")

✓ GOOD: Validate input types
if not all(isinstance(x, (int, float)) for x in height):
    raise TypeError("Height must be numeric")

✓ GOOD: Clear error messages
try:
    img = load_image(path)
except FileNotFoundError:
    print(f"Error: Image not found at {path}")
```

### Performance Tips

```
┌─────────────────────────────────────┐
│ ✓ Use NumPy operations (vectorized) │
│ ✗ Avoid Python loops on arrays      │
│ ✓ Use views when possible (slicing) │
│ ✗ Avoid unnecessary copies           │
│ ✓ Preallocate arrays when known size│
└─────────────────────────────────────┘
```

---

## 📚 Resources

### Official Documentation
- [NumPy Documentation](https://numpy.org/doc/)
- [Pillow (PIL) Documentation](https://pillow.readthedocs.io/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

### NumPy Quick Reference

```python
# Shape operations
arr.shape          # Get dimensions
arr.reshape(2, 3)  # Change shape
arr.flatten()      # Make 1D

# Array operations
arr.sum()          # Sum all elements
arr.mean()         # Average
arr.min(), arr.max()  # Min/max values

# Slicing
arr[start:end]     # Basic slice
arr[::step]        # With step
arr[::-1]          # Reverse
```

### Common Patterns

```python
# Load image
from PIL import Image
img = Image.open("path.jpg")
arr = np.array(img)

# Display image
import matplotlib.pyplot as plt
plt.imshow(arr)
plt.show()

# Save image
img = Image.fromarray(arr)
img.save("output.jpg")
```

---

## 🎯 Learning Tips

1. **Visualize Arrays** - Always print shape before operations
2. **Test Small** - Use small arrays (3x3) to test logic
3. **Check Types** - Use `arr.dtype` to verify data types
4. **Print Shapes** - Debug by printing shapes at each step
5. **Use Comments** - Document array dimensions in comments

---

<div align="center">

### 🚀 Ready to Process Arrays and Images!

**Remember:** Images are just numbers - manipulate them like any data!

---

**Slicing Pattern Cheat Sheet:**
```
arr[row, col, channel]  # 3D image access
arr[y1:y2, x1:x2]      # Crop region
arr[:, :, 0]            # Red channel only
arr[::-1, :, :]         # Flip vertically
arr[:, ::-1, :]         # Flip horizontally
```

Made with ❤️ for Python learners

</div>