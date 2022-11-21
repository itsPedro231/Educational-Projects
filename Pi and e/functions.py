import math

def formula1(steps):
  result = 0

  for x in range(1, steps):
    result += 1/(x**2)
    
  return math.sqrt(result*6)

def formula2(steps):
  result = 0

  for x in range(0, steps):
    y = ((4*x)+1)*((4*x)+3)
    result += 1/y
    
  return result*8  

def factorial(num):
  factorial = 1
  for x in range(num, 1, -1):
    factorial = factorial*x
  
  return factorial
  
def e(num, steps):
  result = 1
  
  for x in range(1, steps):
    d = num**x
    result += d/factorial(x)  
  
  return result ** (1/num)
