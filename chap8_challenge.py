
# 1. Call a different function from the statistics module
import statistics
dir(statistics)
nums = [1,5,33,12,46,33,2]
print(statistics.stdev(nums))

# 2. Create a module named cubed with a function that takes a number as a parameter,
# and returns the number cubed. Import and call the function from another module.

def cubed(x):
    return x**3


