def movexeros(nums):
  z=nums.count(0)
  nums[:]= set(nums)-{0}
  nums.extend([0]*z)

# set(nums)-{0} removes all 0s from the list and returns a set of unique elements
# extend([0]*z) adds the same number of 0s at the end of the list

nums=[1,0,2,0,3,5]
movexeros(nums)
print(nums)
