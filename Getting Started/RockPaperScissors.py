import random

opt = ("rock", "paper", "scissors")

Bot = random.choice(opt)
player = None

while player not in opt:
    player = input("Enter your choice (rock / paper / scissors): ")

print(f"Player: {player.capitalize()}")
print(f"Computer: {Bot.capitalize()}")
