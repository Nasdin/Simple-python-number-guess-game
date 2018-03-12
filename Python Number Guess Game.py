# gold and silver game

old and silver game

import random
import sys
import numpy as np

def get_difficulty():
  print('Enter your desired difficulty level from 1 to 5')
  while True:
    try:
        lv = input()
        if int(lv) < 0 or int(lv) > 5:
            print('Wrong value. Try again.')
            continue
        else:
          return int(lv)
    except ValueError:
        print ('Wrong input. Try again.')
        continue
  
  

def generate_answersheet(difficulty, length, debug=False):
  
  choice_list = list(np.arange(1,difficulty+length))
  
  if debug:
    print("possible numbers:",choice_list)
  
  # get answers
  answers = []
  for i in range(length):
    # append the random number inside
    random_answer = np.random.choice(choice_list)
    answers.append(random_answer)
    choice_list.remove(random_answer)
  
  if debug:
    print ("answers:", str(answers))
  
  return answers
    

def playgame(length=4,debug=False):
  lv = get_difficulty()
  givenList = generate_answersheet(lv,length,debug)
  tries = 0
  gold = 0
  silver = 0
  while gold < length:
      gold = 0
      silver = 0
      print ('Guess a 4-digit number using digits from 1 to ' + str(lv+length-1) + ' only, no digit repeated')
      try:
          guess = input()
          if len(guess) != length:
              print ('You did not enter a {}-digit number. Try again.'.format(length))
              continue
      except ValueError:
          print ('Wrong input. Try again.')
          continue
          
      guess = str(guess)
      guessList = [int(letter) for letter in guess]

      for l in range (length):
          if guessList[l] == givenList[l]:
              gold = gold + 1

      for r in range (length):
          for s in range (length):
              if guessList[r] == givenList[s]:
                 silver = silver + 1
      silver = silver - gold

      print ('You have ' + str(gold) + ' correct digits in the correct place and ' + str(silver) + ' correct digits in the wrong place.')
      tries += 1
  print ('Congratulations! You guessed the number correctly in ' + str(tries) + ' tries!')
  print ('Try again? Type Yes or No.')
  ans = input()
  if ans.lower() == 'yes':
    playgame(length,debug) # recursively starts the function again
     
  elif ans == 'No' or ans == 'no':
      print('Thank you for playing.')
      sys.exit()
  else:
      print ('Invalid Input.')
      sys.exit()
      
playgame(debug = False )
 random
import sys
print('Enter your desired difficulty level from 1 to 5')
lv = input()
lv = int(lv)


while True:    
    a = random.randint(1, lv+4)
    b = random.randint(1, lv+4)
    c = random.randint(1, lv+4)
    d = random.randint(1, lv+4)
    givenList = [a, b, c, d]
    
    while all(givenList.index(v) == i for i, v in enumerate(givenList)):
              
        tries = 0
        gold = 0
        silver = 0
        while gold < 4:
            print ('Guess a 4-digit number using digits from 1 to ' + str(lv+4) + ' only, no digit repeated')
            try:
                guess = input()
            except ValueError:
                print ('Wrong input. Try again.')
                continue            
            guessList = list(guess)
            for v in range (0, 4):
                guessList[v] = int(guessList[v]) 
            
            # print ('Debug: Guessed list is ' + str(guessList))
            
            for l in range (0,4):
                if guessList[l] == givenList[l]:
                    gold = gold + 1
                    
            for r in range (0,4):
                for s in range (0,4):
                    if guessList[r] == givenList[s]:
                       silver = silver + 1
            silver = silver - gold
            
            print ('You have ' + str(gold) + ' correct digits in the correct place and ' + str(silver) + ' correct digits in the wrong place.')
            tries += 1
            if gold != 4:
                gold = 0
                silver = 0
        print ('Congratulations! You guessed the number correctly in ' + str(tries) + ' tries!')
        print ('Try again? Type Yes or No.')
        ans = input()
        if ans == 'Yes':
            print('Enter your desired difficulty level from 1 to 5')
            lv = input()
            lv = int(lv)
            a = random.randint(1, lv+4)
            b = random.randint(1, lv+4)
            c = random.randint(1, lv+4)
            d = random.randint(1, lv+4)
            givenList = [a, b, c, d]
            continue
        elif ans == 'No':
            print('Thank you for playing.')
            sys.exit()
  
            print ('Invalid Input.')
# gold and silver game

import random
import sys
import numpy as np

def get_difficulty():
  print('Enter your desired difficulty level from 1 to 5')
  while True:
    try:
        lv = input()
        if int(lv) < 0 or int(lv) > 5:
            print('Wrong value. Try again.')
            continue
        else:
          return int(lv)
    except ValueError:
        print ('Wrong input. Try again.')
        continue
  
  

def generate_answersheet(difficulty, length, debug=False):
  
  choice_list = list(np.arange(1,difficulty+length))
  
  if debug:
    print("possible numbers:",choice_list)
  
  # get answers
  answers = []
  for i in range(length):
    # append the random number inside
    random_answer = np.random.choice(choice_list)
    answers.append(random_answer)
    choice_list.remove(random_answer)
  
  if debug:
    print ("answers:", str(answers))
  
  return answers
    

def playgame(length=4,debug=False):
  lv = get_difficulty()
  givenList = generate_answersheet(lv,length,debug)
  tries = 0
  gold = 0
  silver = 0
  while gold < length:
      gold = 0
      silver = 0
      print ('Guess a 4-digit number using digits from 1 to ' + str(lv+length-1) + ' only, no digit repeated')
      try:
          guess = input()
          if len(guess) != length:
              print ('You did not enter a {}-digit number. Try again.'.format(length))
              continue
      except ValueError:
          print ('Wrong input. Try again.')
          continue
          
      guess = str(guess)
      guessList = [int(letter) for letter in guess]

      for l in range (length):
          if guessList[l] == givenList[l]:
              gold = gold + 1

      for r in range (length):
          for s in range (length):
              if guessList[r] == givenList[s]:
                 silver = silver + 1
      silver = silver - gold

      print ('You have ' + str(gold) + ' correct digits in the correct place and ' + str(silver) + ' correct digits in the wrong place.')
      tries += 1
  print ('Congratulations! You guessed the number correctly in ' + str(tries) + ' tries!')
  print ('Try again? Type Yes or No.')
  ans = input()
  if ans.lower() == 'yes':
    playgame(length,debug) # recursively starts the function again
     
  elif ans == 'No' or ans == 'no':
      print('Thank you for playing.')
      sys.exit()
  else:
      print ('Invalid Input.')
      sys.exit()
      
playgame(debug = False )

