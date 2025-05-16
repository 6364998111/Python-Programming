def rotate( nums, k):
  """
  Do not return anything, modify nums in-place instead.
  """
  n = len(nums)
  k %= n  # normalize k

  def reverse(left, right):
      while left < right:
          nums[left], nums[right] = nums[right], nums[left]
          left += 1
          right -= 1

  reverse(0, n-1)
  reverse(0, k-1)
  reverse(k, n-1)
  
nums= [1,2,3,4,5,6,7]
k=3
rotate(nums, k)
print(nums)

# Output: [5,6,7,1,2,3,4]
# Time complexity: O(n)
# space complexity: O(1)