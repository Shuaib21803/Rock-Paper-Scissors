import random
import os
import time
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
img = [rock,paper,scissors]
while True:
  print('''Press            0 for Rock
                 1 for Paper
                 2 for Scissors''')
  ch = int(input())
  if ch>=0 and ch<3:
    user_choice = img[ch]
    print("Your choice is: ",img[ch])
    ran = random.randint(0,2)
    print("Computer has played: ",img[ran])
    print("")
    if img[ch]==rock and img[ran]==rock:
      print("TIE!")
    if img[ch]==rock and img[ran]==paper:
      print("Computer WINS!")
    if img[ch]==rock and img[ran]==scissors:
      print("You WIN!")
    if img[ch]==paper and img[ran]==rock:
      print("You WIN!")
    if img[ch]==paper and img[ran]==paper:
      print("TIE!")
    if img[ch]==paper and img[ran]==scissors:
      print("Computer WINS!")
    if img[ch]==scissors and img[ran]==rock:
      print("Computer WINS!")
    if img[ch]==scissors and img[ran]==paper:
      print("You WIN!")
    if img[ch]==scissors and img[ran]==scissors:
      print("TIE!")
    print('''
                 ******************* 
    ''')
    time.sleep(3)
    os.system('clear')
  else:
    print("Please enter valid input")
    time.sleep(1.5)
    os.system('clear')
