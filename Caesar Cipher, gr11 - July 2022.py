# This code Encrypts/Decrypts text using Caesar Cipher

# Caesar Cipher It is a type of substitution cipher in which each letter in the 
# plaintext is replaced by a letter some fixed number of positions down the alphabet.

def encrypt(text, nl):
  text = text.upper()
  
  letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  result = ''
  valueList = []
  diff = []
  for x in range(len(text)):
    if text[x].isalpha():
      for y in range(len(letters)):
        if text[x] == letters[y]:
          valueList.append(y)
    else: 
      diff.append((x,text[x]))
      valueList.append(999)
  
  for x in range(len(valueList)):
    if valueList[x] == 999:
      for y in range(len(diff)):
        for z in range(len(diff[y])):
          if diff[y][z] == x: result += diff[y][z+1]    
    else:  
      result += nl[valueList[x]]
  return result

def decrypt(text,nl):
  text = text.upper()
  nl = nl.upper()
  letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  valueList = []
  result = ''
  diff = []
  for x in range(len(text)):
    if text[x].isalpha():
      for y in range(len(nl)):
        if text[x] == nl[y]:
          valueList.append(y)
    else: 
      diff.append((x,text[x]))
      valueList.append(-1)
  for x in range(len(valueList)):
    if valueList[x] == -1:
      for y in range(len(diff)):
        for z in range(len(diff[y])):
          if diff[y][z] == x: result += diff[y][z+1]    
    else:  
      result += letters[valueList[x]]
        
  return result

x = input('text: ')
nl = input('key (26 different letters): ')
opt = input(' 1 - encrypt \n 2 - decrypt \n 3 - encrypt and decrypt \n >> ')
if opt == '1':
  print(encrypt(x, nl))
elif opt == '2':
  print(decrypt(x,nl))
elif opt == '3':
  x = encrypt(x,nl)
  print('encrypted message:\n ',x)
  y = decrypt(x,nl)
  print('decrypted message:\n',y)


