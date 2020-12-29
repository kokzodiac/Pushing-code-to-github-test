import random
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

human_choice = int(input("Hi, I'm a rock paper scissor bot. Type 0 for rock, 1 for paper, and 2 for scissor.\n"))


choice = [rock, paper, scissors]
output_human_choice = choice[human_choice]
bot_choice = random.randint(0,2)
output_bot_choice = choice[bot_choice]


print("You chose: \n")
print(output_human_choice)
print("Computer chose: \n")
print(output_bot_choice)

if (bot_choice - human_choice) == 0: 
    print("It's a tie. We're gonna get them next time. ")
elif (bot_choice - human_choice) == -1 or (bot_choice - human_choice) == 2:
    print("You win.")
else:
    print("You lose.")
    


