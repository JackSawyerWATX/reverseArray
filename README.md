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

## Function Documentation

### `reverseArray(arr)`

**Description:**
Reverses the order of elements in an array and returns a new array with elements in reverse order.

**Parameters:**
- `arr` (list): The input array/list of integers to be reversed

**Returns:**
- `list`: A new list containing the elements of the input array in reverse order

**Time Complexity:** O(n) where n is the length of the array
**Space Complexity:** O(n) for creating a new reversed array

**Example Usage:**
```python
# Basic usage
result = reverseArray([1, 2, 3, 4, 5])
print(result)  # Output: [5, 4, 3, 2, 1]

# With different data types (works with any list)
result = reverseArray([10, 20, 30])
print(result)  # Output: [30, 20, 10]

# Single element
result = reverseArray([42])
print(result)  # Output: [42]

# Empty array
result = reverseArray([])
print(result)  # Output: []
```

## Implementation Details

The primary solution uses Python's slicing notation for array reversal:

```python
def reverseArray(arr):
    return arr[::-1]
```

**How it works:**
- `arr[:]` - Creates a slice of the entire array
- `[::-1]` - Steps through the slice with a step of -1 (backwards)
- This creates a new list without modifying the original

### Alternative Implementation Methods

The project demonstrates several approaches to array reversal:

#### 1. **Slicing Method** (Current implementation)
```python
def reverseArray(arr):
    return arr[::-1]
```
- **Pros:** Concise, Pythonic, readable
- **Cons:** Creates a new list (uses extra memory)
- **Best for:** Most general use cases

#### 2. **Built-in `reversed()` Function**
```python
def reverseArray(arr):
    return list(reversed(arr))
```
- **Pros:** Explicit intent, works with any iterable
- **Cons:** Slightly less efficient than slicing
- **Best for:** When working with different iterable types

#### 3. **In-place Reversal**
```python
def reverseArray(arr):
    arr.reverse()
    return arr
```
- **Pros:** Memory efficient (modifies original)
- **Cons:** Modifies the original array
- **Best for:** When you want to modify the original array

#### 4. **Manual Two-Pointer Approach**
```python
def reverseArray(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
```
- **Pros:** Educational value, shows algorithm concept
- **Cons:** More verbose, modifies original array
- **Best for:** Understanding the underlying algorithm

## Requirements

- Python 3.x

## Origin

This exercise was originally from HackerRank and was completed as coding practice to understand different array manipulation techniques in Python.

## Learning Objectives

- Understanding Python list slicing
- Array/List manipulation
- Different approaches to solving the same problem
- Code optimization and readability

### I love you all! Happy coding!