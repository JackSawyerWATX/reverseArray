def reverseArray(arr):
  return arr[::-1]
print(reverseArray([1, 2, 3, 4, 5, 6, 7]))
  # creates a new list without modifying the original

def reverseArray(arr):
  return list(reversed(arr))
print(reverseArray([48, 47, 46, 45, 44, 43, 42]))
  # Best used when working with different iterable types

def reverseArray(arr):
  arr.reverse()
  return arr # must have return statement with this method
print(reverseArray([10, 20, 30, 40, 50, 60, 70]))
  # Best to use when you want to modify the original array

def reverseArray(arr):
  left, right = 0, len(arr) - 1
  while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
  return arr # must have return statement with this method
print(reverseArray([195, 185, 175, 165, 155, 145, 135]))
# Best to use in understanding the underlying algorithm