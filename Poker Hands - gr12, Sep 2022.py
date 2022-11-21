import random

# this code generates a 5 random cards poker hand and checks what is the highest combination

def checkHand(hand):
  rank = []
  suit = []
  for x in hand:
    rank.append(x[0])
    suit.append(x[1])
    
  y = 0
  suitSum = -1
  rankSum = 1
  highSum = 0
  
  #rank sum
  rankList = []
  for x in range(len(rank)):
    for z in range(len(rank)):
      if rank[x] == rank[z] and z != x: 
        rankSum += 1
        
    if rankSum >= 2:
      flag = True
      
      for z in range(len(rankList)):
        if rank[x] == rankList[z][0]:
          flag = False
          
      if flag:    
        rankList.append((rank[x], rankSum))
      if highSum < rankSum:
        highSum = rankSum
        
    rankSum = 1  
    
  y = 0  
  #suit sum
  for x in range(len(suit)):
    for z in range(len(suit)):    
      if suit[x] == suit[z] and z != x: 
        y+=1
    
    if y > suitSum:
      suitSum = y
    y = 1

  #check sequence
  values = [('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('J', 11), ('Q', 12), ('K', 13), ('A', 14)]
  order = []
  
  #Sorting hand
  for y in range(len(rank)):
    for x in range(len(values)):
      if rank[y] == values[x][0]:
        order.append(values[x][1])
  
  order.sort()      
  rank = []
  for x in range(len(order)):
    for y in range(len(values)):
      if values[y][1] == order[x]:
        rank.append(values[y][0])

  #checking sequence
  sequence = False
  
  if order[0] + 4 == order[4] and order[1] + 3 == order[4] and order[2] + 2 == order[4] and order[3] + 1 == order[4]:
    sequence = True
  
  royalSum = 0
  for x in rank:
    if x == 'A' or x == 'K' or x == 'Q' or x == 'J' or x == '10':
      royalSum +=1

  checking = 0
  for x in rankList:
    if x[1] == 2: checking += 1
    if x[1] == 3: checking += 3 
      
  if suitSum == 5 and royalSum == 5: print('WOW! Royal Flush')
  elif suitSum == 5 and sequence: print('WOW! Straight Flush')
  elif highSum == 4: print('WOW! Four of a kind')
  elif checking >= 4: print('WOW! Full House')
  elif suitSum == 5: print('WOW! Flush')
  elif sequence: print('WOW! Straight')
  elif highSum == 3: print('WOW! Three of a kind')
  elif checking == 2: print('WOW! Two Pairs')
  elif highSum == 2: print('WOW! Pair')
  else: print(rank[4], 'High card')
    
hand = []
while len(hand) < 5:
  card = random.randint(0,51)
  suit = card // 13  # Gives the quotient, finds the suit
  rank = card % 13   # Gives the remainder, finds the number
  suits  = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
  ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

  if (ranks[rank], suits[suit]) not in hand:
    hand.append((ranks[rank], suits[suit]))
  
for x in range(len(hand)):
  print(hand[x][0], 'of', hand[x][1])

print('-----------')  
checkHand(hand)
