# This code contains 3 different variations of Blackjack - Twenty One, Multi Heap and Whythoff's Game

from random import randint

def twentyOne():
  heap = 1
  p = 1
  while heap < 21:
    print('')
    print('heap:', heap, '\n')
    print('player', p, "turn:")
    while True:
      if heap < 18:
        x = input('how many objects do you want to add? (1-3): ')
        if int(x) > 0 and int(x) < 4:
          heap += int(x)
          break
      elif heap == 18:
        x = input('how many objects do you want to add? (1-2): ')
        if int(x) > 0 and int(x) < 3:
          heap += int(x)
          break     
      elif heap == 19:
        x = input('how many objects do you want to add? (1): ')
        if int(x) == 1:
          heap += int(x)
          break  
    if heap == 20:
      print('player', p, 'wins!')
      break
    if p == 1:
      p = 2
    else: p = 1  
def multiHeap():
  p = 1
  heap1 = randint(2,100)
  heap2 = randint(2,100)
  heap3 = randint(2,100)
  while True:
    print('')
    print('player', p, 'turn:')
    print('heap 1:', heap1)
    print('heap 2:', heap2)
    print('heap 3:', heap3)
    c = input('which heap? (1-3): ')
    if c == '1':
      a = heap1
      if a == 1: 
        print('')
        print("it is already one!")
        continue  
    elif c == '2':
      a = heap2
      if a == 1:
        print('')
        print("it is already one!")
        continue  
    elif c == '3':
      a = heap3
      if a == 1:
        print('')
        print("it is already one!")
        continue
    while True:
      if a == 2:
        x = input('how many objects do you want to remove? (1): ')
        if int(x) == 1:
          a -= int(x)
          break
        else: continue
      elif a > 2:
        x = input('how many objects do you want to remove? (1-'+str(a-1)+'): ')
        if int(x) > 0 and int(x) < a:
          a -= int(x)
          break
        else: continue  
    if c == '1': heap1 = a
    elif c == '2': heap2 = a
    elif c == '3': heap3 = a
    if heap1 + heap2 + heap3 == 3:
      print('heap 1:', heap1)
      print('heap 2:', heap2)
      print('heap 3:', heap3,'\n')
      print('player', p, 'wins!')
      break
    if p == 1:
      p = 2
    else: p = 1  
def wtoff():
  p = 1
  f = 0
  heap1 = randint(2,100)
  heap2 = randint(2,100)
  while True:
    print('')
    print('player', p, 'turn:')
    print('heap 1:', heap1)
    print('heap 2:', heap2)
    bs = input('both or single heap? (both-single): ')
    if bs == 'both':
      a = heap1
      b = heap2
      if a == 1: 
        print('')
        print("heap 1 is already one!")
        continue
      if b == 1:
        print('')
        print('heap 2 is already one!')
        continue
      if a > f: 
        f = a
        if b <= f: f = b
      while True:    
        x = input('how many objects do you want to remove from both heaps? (1-'+str(f-1)+'):')
        if int(x) > 1 and int(x) < f:
          a -= int(x)
          b -= int(x)
          break
      heap1 = a 
      heap2 = b
      if heap1 + heap2 == 2:
        print('heap 1:', heap1)
        print('heap 2:', heap2,'\n')
        print('player', p, 'wins!')
        break  
    elif bs == 'single':
      while True:
        print('')
        c = input('which heap? (1-2): ')
        if c == '1':
          a = heap1
          break
        elif c == '2':
          a = heap2
          break
        else: continue  
      if a == 1:
        print('')
        print("it is already one!")
        continue   
      while True:
        if a == 2:
          x = input('how many objects do you want to remove? (1): ')
          if int(x) == 1:
            a -= int(x)
            break
          else: continue
        elif a > 2:
          x = input('how many objects do you want to remove? (1-'+str(a-1)+'): ')
          if int(x) > 0 and int(x) < a:
            a -= int(x)
            if c == '1': heap1 = a
            elif c == '2': heap2 = a
            break
          else: continue
    if bs != 'single' and bs != 'both':
      continue
    if heap1 + heap2 == 2:
      print('heap 1:', heap1)
      print('heap 2:', heap2,'\n')
      print('player', p, 'wins!')
      break
    if p == 1: p = 2
    else: p = 1

def menu():
  print(' ----menu----\n')
  print('1 - twenty-one')
  print('2 - multi-heap nim')
  print("3 - wythoff's game")
  x = input('type the number: ')
  if x == '1': twentyOne()
  elif x == '2': multiHeap()  
  elif x == '3': wtoff()
menu()
