import random
import os
import time

Ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
Scores = [1,2,3,4,5,6,7,8,9,10,10,10,10]
Suits = ['\u2660','\u2665','\u2663','\u2666']

Cards = []

#-----------------------------------------

def ResetCards():
    global Cards
    global PlayerHand
    global Score
    global DealerScore
    global Action
    global DealerHand

    Score = 0
    DealerScore = 0
    Action = '*'
    PlayerHand = []
    DealerHand = []
    Cards = []   # 0..51, 52 is a dummy card
    for c in range(0,52):
        Cards.append(False)  #Append 52 "False" and 1 "True" 
    Cards.append(True)
    

#------------------------------------------

def DrawCard(Hand):
    num1 = 52

    while Cards[num1]: #Card is already drawn if True
        num1 = random.randint(0,51) #Repeat until an undrawn card is selected

    Cards[num1] = True

    Hand.append(num1)

    return num1

#-----------------------------------------
#-----------------------------------------
    
def DisplayHand():
    r = ''
    Score = 0
    os.system('clear')
    print('Player Hand:')
    for c in range(len(PlayerHand)):
        r = r + '['+Ranks[PlayerHand[c]%13]+Suits[PlayerHand[c]//13]+']'
        Score = Score + Scores[PlayerHand[c]%13]
    r = r + '   Score: '+str(Score)+'\n'
    print(r)
    
    return Score
#-----------------------------------------
def DisplayDealerHand():
    r = ''
    DealerScore = 0
    for c in range(len(DealerHand)):
        r = r + '['+Ranks[DealerHand[c]%13]+Suits[DealerHand[c]//13]+']'
        DealerScore = DealerScore + Scores[DealerHand[c]%13]
    r = r + '   Score: '+str(DealerScore)
    print(r)

    return DealerScore
    
    
#-----------------------------------------    
#-----------------------------------------
def DealerPlay():
    print()
    print('Dealer Plays:  ')
    DrawCard(DealerHand)
    DrawCard(DealerHand)
    S = DisplayDealerHand()

    while S < 17:
        time.sleep(1)
        DrawCard(DealerHand)
        S = DisplayDealerHand()
        

    
    return S
    
#-----------------------------------------
def GetAction():
    Action = '*'
    while not Action in ['D','d','S','s']:
        Action = input('[D]raw or [S]tay?  ')

    Action = Action.upper()
    return Action
#-----------------------------------------
def SplashScreen():
    print('Welcome to 21!')
    print('--------------')
    print()
    for c in range(0,8):
        print(Suits[c%4]+' ',end='')
    print()
    print()
    print('Rules: ')
    print('Draw cards but don\'t go over 21!')
    print('A = 1, JQK = 10')
    print('Dealer draws on 16 or less, stays on 17 or more')
    print('First 21 or high score wins')
    print('Dealer wins on a tie')
    print()
    print()
    temp = input('Press <ENTER> to continue...')
    os.system('clear')
#-----------------------------------------
def Main(w,l):
    
  ResetCards()
  DrawCard(PlayerHand)
  DrawCard(PlayerHand)
  PScr = DisplayHand()
  x = True
  
  while True:   #Player chooses to draw or stay
      Act = GetAction()
      if (Act == 'S'):
          break
      else:
          DrawCard(PlayerHand)
          PScr = DisplayHand()
          
      if PScr >= 21:
          break
  
  if PScr == 21:
      print('You Win!')
      w += 1
  elif PScr > 21:  
      print('You Lose!')  
      l+=1
  else:  #Dealer must draw
      
      DScr = DealerPlay()
  
      if DScr > 21:
          print('You Win!')
          w += 1
      elif PScr > DScr:
          print('You Win!')
          w += 1
      else:
          print('You Lose!')
          l+=1

  print()
    
  print('w:',w,'l:',l)
  temp = input('Press <ENTER> to continue or Q to quit...')
  
  if temp == 'q' or temp == 'Q':
    x = False
  return w, l, x

#-----------------------------------------
def score():
  print('\n ----- score ----- ')
  with open('scoreList.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
      print(line)




SplashScreen()
x = True
w = 0
l = 0
while x:
  
  w, l, x = Main(w,l)
  

print('saving score...')
time.sleep(1)
name = input('insert your name: ')
highScore = []

with open('scoreList.txt', 'r') as file:
  lines = file.readlines()
  for line in lines:
    pos = line.find(' ')    
    names = line[0:pos]
    values = line[pos+1:len(line)].replace('\n','')
    highScore.append((names, values)) 

def insertScore(name, score):

  for c in range(0,10):
    if int(highScore[c][1]) <= w:
      highScore.insert(c, (name, w))
      highScore.pop(10)
      break

if w >= int(highScore[9][1]):  #Insert the score
  print(name,w)
  insertScore(name, w)    

with open('scoreList.txt','w') as f:

  for c in range(len(highScore)):
    r = highScore[c][0]+' '+str(highScore[c][1])
    if c != len(highScore)-1: 
      r = r + '\n'
    f.write(r)
    
score()
