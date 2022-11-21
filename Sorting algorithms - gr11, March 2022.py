import random
from datetime import datetime
y = []
for x in range(0,10): #Generates a list of ten unsorted random numbers
  y.append(random.randrange(0,100))
print("unsorted list:", y)
y2 = y
y3 = y
y4 = y
y5 = y
def insertion(y):
  for x in range(0, len(y)):
    z = 0
    while y[z] < y[x]:
      z += 1
    e = y[x]
    y.pop(x)
    y.insert(z, e)
  return y  

def selection(y): # Selection sort algorithm
  for x in range(0,len(y)):
    e = 9999999999
    for b in range(x, len(y)): 
      if y[b] < e:   
        e = y[b]  
        to_pop = b
        y.pop(to_pop)
        y.insert(x, e)
  return y      

def bubble(y): # Bubble sort algorithm
  list1 = []
  for c in range(0,len(y)):
    for x in range(0,len(y)):
      try:
        if y[x] > list1[x+1]:
          e = y[x]
          y[x] = y[x+1]
          y[x+1] = e
      except: continue
  return y      

def recursive(x): #recursive sort algorithm. Sorts from the biggest to the smallest number
  if len(x) > 1:
    e = -1
    for c in range(0, len(x)):
      if x[c] > e: e = x[c]
    biggest = [e]    
    x.remove(e) 
    result = biggest + recursive(x)
  else: result = x
  return result
        
before = datetime.now()
print(insertion(y2))
after = datetime.now()

before1 = datetime.now()
print(selection(y3))
after1 = datetime.now()

before2 = datetime.now()
print(bubble(y4))
after2 = datetime.now()

before3 = datetime.now()
print(recursive(y5))
after3 = datetime.now()

print("\ntime that each algorithm took to sort:")
print('insertion', after - before)
print('selection', after1 - before1)
print('bubble', after2 - before2)
print('recursive', after3 - before3)
