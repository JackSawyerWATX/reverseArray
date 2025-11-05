def reverseArray(arr):
  return arr[::-1]
print(reverseArray([1, 2, 3, 4, 5]))

def reverseArray(arr):
  return list(reversed(arr))
print(reverseArray([48, 47, 46, 45, 44, 43, 42]))

def reverseArray(arr):
  arr.reverse()
  return arr # must have  return statement with this method
print(reverseArray([10, 20, 30, 40, 50]))