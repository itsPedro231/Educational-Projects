# This code Encrypts/Decrypts text using Caesar Cipher

# Caesar Cipher It is a type of substitution cipher in which each letter in the 
# plaintext is replaced by a letter some fixed number of positions down the alphabet.

import os
def encrypt(text,n):
  result = ""

  for x in range(len(text)):
    char = text[x]
    n = int(n)
    
    if char.isalpha():
      result += chr((ord(char) + n - 65) % 26 + 65)
    else: result += char  
    
  return result

def decrypt(text,n):
  result = ""

  for x in range(len(text)):
    char = text[x]
    n = int(n)
    
    if char.isalpha():
      result += chr((ord(char) - n - 65) % 26 + 65)
    else: result += char  
    
  return result
  
x = str(input('text: '))
x = x.upper()
n = str(input('number: '))
y = input(' 1 - decrypt \n 2 - encrypt \n 3 - encrypt and decrypt \n >> ')
os.system('clear')
print("\nPlain Text : " + x)
print("Shift pattern : " + str(n))

if y == '1':
  print('\ndecrypted message:\n', decrypt(x,n))
elif y == '2':
  print('\nencrypted message:\n', encrypt(x,n))
elif y == '3':
  x = encrypt(x,n)
  
  print('\nencrypted:\n', x)
  print('\ndecrypted:\n', decrypt(x,n))
  
