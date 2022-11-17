import os
import random
import math
import click

def print_board(aboard):
  print()
  print(' '+aboard[0]+' ║ '+aboard[1]+' ║ '+aboard[2])
  print('═══╬═══╬═══')
  print(' '+aboard[3]+' ║ '+aboard[4]+' ║ '+aboard[5])
  print('═══╬═══╬═══')
  print(' '+aboard[6]+' ║ '+aboard[7]+' ║ '+aboard[8])
  print()

def SpaceIsFree(spot, aboard):
  return aboard[spot] == ' '

def PlayerMove(aboard):
  spot = Get_Spot(aboard)
  Add_To_Board(aboard, spot, 'X')

def Get_Spot(aboard):
  flag = False
  spot = '*'
  
  while not flag:
    while not spot in ['1','2','3','4','5','6','7','8','9']:
      spot = input('Choose a spot to play:  ')
    spot = int(spot) -1  #Return 1 less so that it matches the list indices
                         #Example, spot 9 is index 8, spot 1 is index 0
    flag = SpaceIsFree(spot,aboard)
  return(spot)

def Add_To_Board(aboard, spot, turn):
  aboard[spot] = turn  

def IsWinner(aboard, letter):
  flag = False

  if aboard[0] == letter and aboard[1] == letter and aboard[2] == letter:  flag = True
  if aboard[3] == letter and aboard[4] == letter and aboard[5] == letter:  flag = True
  if aboard[6] == letter and aboard[7] == letter and aboard[8] == letter:  flag = True
  if aboard[0] == letter and aboard[3] == letter and aboard[6] == letter:  flag = True
  if aboard[1] == letter and aboard[4] == letter and aboard[7] == letter:  flag = True
  if aboard[2] == letter and aboard[5] == letter and aboard[8] == letter:  flag = True
  if aboard[0] == letter and aboard[4] == letter and aboard[8] == letter:  flag = True
  if aboard[6] == letter and aboard[4] == letter and aboard[2] == letter:  flag = True       
  return flag

def ComputerMoveRandom(aboard):
  Possible_Moves = []

  for c in range(0,9):
    if SpaceIsFree(c,aboard):
      Possible_Moves.append(c)
      
  if len(Possible_Moves) > 0:
    return random.choice(Possible_Moves)
  else:
    return -1

def cMoves2(aboard):
  possibleMoves = []

  for c in range(0,9):
    if SpaceIsFree(c,aboard):
      possibleMoves.append(c)
    cornerMoves = []
  if 0 in possibleMoves: cornerMoves.append(0)
  if 2 in possibleMoves: cornerMoves.append(2)
  if 6 in possibleMoves: cornerMoves.append(6)
  if 8 in possibleMoves: cornerMoves.append(8)

  if len(cornerMoves) > 0:
    return random.choice(cornerMoves)
  else: return random.choice(possibleMoves)

def findx(aboard):
  countx = 0
  position = 0
  for c in range(0,9):
    if aboard[c] == 'X': 
      countx +=1
      position = c
  if countx != 1: return -1
  else: return position  

def cMoves3(aboard):
  xspot = findx(aboard)
  if xspot == -1:
    return cMoves2(aboard)
  elif xspot in [0,2,6,8]: return 4
  else: return cMoves2(aboard)

def cMoves4(aboard):
  if aboard[0] == 'X' and aboard[8] == ' ': return 8
  elif aboard[2] == 'X' and aboard[6] == ' ': return 6
  elif aboard[8] == 'X' and aboard[0] == ' ': return 0
  elif aboard[6] == 'X' and aboard[2] == ' ': return 2
  else: return cMoves3(aboard)  

def cMoves5(aboard):
  possibleMoves = []
  for c in range(0,9):
    if SpaceIsFree(c,aboard):
      possibleMoves.append(c)

  move = -1

  #Check for a winning move for 'O'
  for pm in possibleMoves:
    tempboard = aboard + []
    tempboard[pm] = 'O'
    if IsWinner(tempboard,'O'):
      move = pm
    tempboard[pm] = ' '

  if move != -1:
    return move
  else: 
    return cMoves4(aboard)

def minimax(Maximizing, Player, board):
  
  if  IsWinner(board,'O'):  return 10
  elif IsWinner(board,'X'):  return -10
  elif IsTie(board):  return 0
  else:  pass #Board is not full, not a tie, no winner  
  Scores = []
  PossibleMoves = []
  
  for c in range(0,9):
    if SpaceIsFree(c, board):
      PossibleMoves.append(c)

  for move in PossibleMoves:
    tempboard = board + []
    if Maximizing:    # O is playing
      Add_To_Board(tempboard, move, 'O' )
      Player = 'X'
    else:
      Add_To_Board(tempboard, move, 'X')
      Player = 'O'

    Scores.append(minimax(not Maximizing, Player, tempboard))
    Add_To_Board(tempboard, move, ' ') #remove the play
  
  if Maximizing: return max(Scores)
  else: return min(Scores)

def cBestMove(board):
  bestScore = -math.inf
  bestMove = None

  PossibleMoves = []
  
  for c in range(0,9):
    if SpaceIsFree(c, board):
      PossibleMoves.append(c)
  
  for move in PossibleMoves:  #Computer move, "O" is moving
    tempboard = [] + board  
    Add_To_Board(tempboard, move, 'O')
    
    score = minimax(False, 'X', tempboard)
        
    tempboard[move] = ' '
      
    if (score > bestScore):
      bestScore = score
      bestMove = move

  return bestMove    
    
def IsBoardFull(aboard):
  flag = True
  
  for c in range(0,len(aboard)):
    if aboard[c] == ' ':
      flag = False

  return flag 

def IsTie(aboard):
  if IsBoardFull(aboard) and not IsWinner(aboard,'X') and not IsWinner(aboard,'O'):
    return True
  else: 
    return False

def Main(board):
  print('Welcome to Tic Tac Toe')
  print('    by PEDRO')
  splash = ["T","I","C","T","A","C","T","O","E"]
  print_board(splash)
  pause = input('Press <ENTER> to continue...')
  #End of intro screen

  while not IsBoardFull(board):  #Game continues until board is full
    os.system('clear')
    print_board(board)
    
    if not(IsWinner(board,'O')):  #Player 'X' can go
      PlayerMove(board)
      
    os.system('clear')
    print_board(board)

    if IsWinner(board,'X'):
      break

    if IsTie(board):
      break

    if not(IsWinner(board,'X')):   #Computer 'O' can go
      move = cBestMove(board)
      #move = ComputerMoveAlgorithm2(board)
      if IsTie(board): #no move available
        #print('Tie Game')
        break

      else:
        Add_To_Board(board, move, 'O')
        os.system('clear')
        print_board(board)

        if not IsWinner(board,'O'):
          pause = input('Computer plays spot '+str(move+1)+'\nPress <ENTER> to continue...')
          #print Move +1 to change the index into 1-9
      if IsWinner(board,'O'):
        break
        
      if IsTie(board):
        break

Board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
Main(Board)

if IsTie(Board):
  print('It\'s a tie!')
elif IsWinner(Board,'X'):
  print('You win!')
elif IsWinner(Board,'O'):
  print('Computer wins!')
else:
  pass
