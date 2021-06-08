import os
from art import logo
print(logo)
dictionary={}
repeat=True
while repeat==True:
  name=input('Type your name: ')
  bid= input('What is the bid price: $')
  try:
        bid=int(bid)
  except:
        print('Wrong keyword please type again!')
        continue  
              
  
        
  dictionary[name]=bid
  other=input('Any other user who wants to bid? Yes or no.: ').lower()
  if other != 'yes':
    repeat=False
  else:
    os.system('cls')
maximum = max(dictionary, key=dictionary.get)  
print(maximum, dictionary[maximum])