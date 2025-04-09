#higher order function means a function that takes another function as an argument or returns a function as its result.

def squares_of_array(fuc,arr):
  return [fuc(x) for x in arr]

def square(x):
  return x**2

arr=[1,2,3,4,5]
print(squares_of_array(square,arr))
# The above code defines a function squares_of_array that takes a function fuc and an array arr as arguments.
# It applies the function fuc to each element of the array arr and returns a new array with the results.


#using map

def cube(x):
  return x**3

cube_array=list(map(cube,arr))
print(cube_array)

# using filter

def is_even(x):
  return x%2 == 0

even_array=list(filter(is_even,arr))
print(even_array)
# The above code defines a function is_even that checks if a number is even.

# using reduce
from functools import reduce
def add(x,y):
  return x+y 

sum_of_array=reduce(add,arr)
print(sum_of_array)