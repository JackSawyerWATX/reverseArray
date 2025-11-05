# Reverse Array

## Overview

This project contains a Python implementation of an array reversal function, originally practiced from a HackerRank coding challenge. The solution demonstrates different approaches to reversing arrays in Python.

## Problem Description

The task is to implement a function that takes an integer array as input and returns a new array with the elements in reverse order.

**Example:**
- Input: `[1, 4, 3, 2]`
- Output: `[2, 3, 4, 1]`

## Files

- `reverse.py` - **Main file to run** - Simple implementation with test cases
- `revArr.py` - HackerRank template format (requires environment setup)
- `test_revArr.py` - Test file with multiple test cases

## How to Run

To run the program from the terminal:

```bash
python reverse.py
```

This will execute the `reverseArray` function with predefined test cases and display the results.

## Implementation

The solution uses Python's slicing notation for array reversal:

```python
def reverseArray(arr):
    return arr[::-1]
```

### Alternative Approaches

The project also includes several other methods for reversing arrays:

1. **Slicing** (Current implementation): `arr[::-1]`
2. **Built-in function**: `list(reversed(arr))`
3. **In-place reversal**: `arr.reverse()`
4. **Manual two-pointer approach**: Swap elements from both ends

## Requirements

- Python 3.x

## Origin

This exercise was originally from HackerRank and was completed as coding practice to understand different array manipulation techniques in Python.

## Learning Objectives

- Understanding Python list slicing
- Array/List manipulation
- Different approaches to solving the same problem
- Code optimization and readability