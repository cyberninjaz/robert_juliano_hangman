import random

nums = []

def arrayaddup(arr) : 
    finval = 0
    for f in range(0, 20) :
        finval += arr[f]
      #  print(finval)
    return finval


for i in range(0, 20):
    x = random.randint(0,101)
    nums.insert(i, x)
print(nums)
print(arrayaddup(nums))


