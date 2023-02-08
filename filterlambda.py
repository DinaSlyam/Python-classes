# importing math library
import math

# creating function
def main(x):

# checking for negative numbers
     if x <= 1:
          return False

#  for loop to iterate through number range to find its root if exist
for i in range(2, int(math.sqrt(x)) + 1):
    if x % i == 0:
        return False

# else return true
return True

# using filter function
print(list(filter(main, range(30))))