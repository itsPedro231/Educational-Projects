# formulas to get aproximate numbers of Pi and euler's number

import Functions
import math


print("Pi:", math.pi)
print('-----------------')

print("first formula, 100 steps:", Functions.formula1(100))
print("first formula, 10000 steps:", Functions.formula1(10000))
print("first formula, 1000000 steps:", Functions.formula1(1000000))

print('-----------------')

print("second formula, 100 steps:", Functions.formula2(100))
print("second formula, 10000 steps:", Functions.formula2(10000))
print("second formula, 1000000 steps:", Functions.formula2(1000000))

print('-----------------')

print("e, 100 steps:", Functions.e(3, 100))
# print("e, 10000 steps:", Functions.e(3, 10000)) #It takes a long time
# print("e, 1000000, steps:", Functions.e(3, 1000000)) #It takes a really long time
