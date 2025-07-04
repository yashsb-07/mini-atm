""" Number Guessing Game """

import random

target = random.randint(1,10)

while True:
    user_ch = input("Enter you guessing number or quit(Q): ")
    if user_ch == "Q":
        break
    
    user_ch = int(user_ch)
    print(user_ch)
    if user_ch == target:
        print("..Congratulations..Your guess is correct.")
        break
    
    if(user_ch > target):
        print("..your guess is to big.. Try to guesss small number.")
        
    else:
        print("...your guess is very small.. Try to guess big number.")
        
print("\n------GAME OVER-----")