def removeDuplicates(nums):
  nums[:] = sorted(set(nums))
  return len(nums)

#[:] is used to modify the original list

nums= [1, 1, 2]
print(removeDuplicates(nums))

# time complexity: O(nlogn)
# space complexity: O(n)