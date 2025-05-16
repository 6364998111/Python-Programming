def check(nums):
  count=0
  n=len(nums)
  for i in range(n):
      if nums[i] > nums[(i+1)%n]:
          count+=1
      if count > 1:
          return False
  return True

# 🔍 Iterate through the array and check each adjacent pair
# ⭕ Use modulo operator (%) for wrap-around handling (like connecting the last and first elements)
# 📝 Count places where order breaks (current element > next element)
# ❌ If we find more than one break, return false (impossible to sort with one rotation)
# ✅ If only one or zero breaks found, return true (possible to sort!)

nums=[3,4,5,1,2]
print(check(nums))

# time complexity: O(n)
# space complexity: O(1)