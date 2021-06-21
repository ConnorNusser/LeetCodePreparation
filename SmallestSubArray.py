def smallest_subarray_with_given_sum(s, arr):
  window_start = 0
  min_length = len(arr) + 1
  window_sum = 0
  for i in range(len(arr)):
    window_sum = window_sum + arr[i]

    while window_sum >= s:
      min_length = min(min_length, i - window_start + 1)
      window_sum = window_sum - arr[window_start]
      window_start = window_start + 1
  if min_length == len(arr) + 1:
    return 0
  return min_length