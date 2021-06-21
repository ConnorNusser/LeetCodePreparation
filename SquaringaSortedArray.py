def make_squares(arr):
  val = len(arr)
  left_ptr = 0
  right_ptr = val - 1
  squares = [0 for x in range(val)]
  highestSquareIdx = val - 1
  while highestSquareIdx !=  -1:
    if (arr[left_ptr] ** 2) > (arr[right_ptr] ** 2):
      squares[highestSquareIdx] = arr[left_ptr] ** 2
      left_ptr = left_ptr + 1
    else:
      squares[highestSquareIdx] = arr[right_ptr] ** 2
      right_ptr = right_ptr - 1
    highestSquareIdx = highestSquareIdx - 1

  return squares
