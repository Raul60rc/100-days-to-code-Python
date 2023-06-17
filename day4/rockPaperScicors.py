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

game_images = ["rock", "paper", "scissors"]

player = input("Enter your choice (Rock/Paper/Scissors): ").lower()
computer = (random.choice(game_images))

if player == "rock" and computer == "paper":
    print(f"Rock beats paper! {game_images[0]}")
elif player == "scissors" and computer == "paper":
    print(f"Scissors beats paper!{game_images[2]}")
elif player == "paper" and computer == "rock":
    print(f"paper beats rock!{game_images[1]}")
elif player == "rock" and computer == "scissors":
    print(f"rock beats scissors{game_images[0]}")
