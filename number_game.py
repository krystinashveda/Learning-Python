# import random
from random import randint
secret_num = randint(1,10)

def game():
	guess = input("Guess the number ")
	guessed_number = int(guess)
	if guessed_number == secret_num:
		print("You win!")
	else:
		print("Try again")
		game()

game()
