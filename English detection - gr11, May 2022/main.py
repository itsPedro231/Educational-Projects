# this code gets a text sample and checks if it is written in English
# it checks a 10000 word list to detect if the text is written in English
def readFile():
  file = open('10000 English Words Frequency Ranked.txt')
  wordList = []  
  newLine = ''
  lines = file.readlines()
  for line in lines:
    for word in line:
      if word.isalpha():
        newLine += word
    wordList.append(newLine)
    newLine = ''
  file.close()    
  return wordList  

englishWords= readFile()

text = input('text: ').upper()
temp = text.split(' ')
count = 0
for x in temp:
    for word in englishWords:
      word = word.upper()
      if x == word:
        count += 1
        break
print('\n' + text)   
print(count, 'recognized words')
print(str((count/len(temp))*100) + '% English')
        
