import os
import sys
import random

word = ""
count_play = 0
count_win = 0
topic = [
    ["Russia","Germany","United Kingdom","France","Italy","Spain","Ukraine","Poland","Netherlands","Finland","Vietnam","Thailan","Laos","Campodia","China"],
    ["Audi","BMW","Bentley","Chevrolet","Dodge","Ford","Honda","Hyundai","Infiniti","Jaguar","Jeep","Kia","Land Rover","Lexus","Lincoln"],
    ["Dog","Bear","Elephant","Polar bear","Turtle","Tortoise","Crocodile","Rabbit","Porcupine","Har","Hen","Pigeon","Albatross","Crow","Fish"],
    ["apples","pears","oranges","grapefruits","mandarins","limes","apricots","peaches","plums","tropical","exotic","bananas","mangoes","berries","strawberries"]
]



def topic1():
	global usrTopic
	usrTopic = input("Player 1 enter topic number(1-4): \ntype 1 for Country topic! \ntype 2 for Car brand topic! \ntype 3 for Animal topic! \ntype 4 for Fruit topic!\n")
	if usrTopic == "1":
		os.system("cls")
		print("The topic is: Country")
	elif usrTopic == "2":
		os.system("cls")
		print("The topic is: Car brand")
	elif usrTopic == "3":
		os.system("cls")
		print("The topic is: Animal")
	elif usrTopic == "4":
		os.system("cls")
		print("The topic is: Fruit")
	else:
		os.system("cls")
		topic1()


def operator():
	os.system("cls")
	print("1. Play\n2. Exit")
	urChoice = input("Option: ")	
	while True:
		if urChoice == "1":
			os.system("cls")
			topic1()
			word = random.choice(topic[int(usrTopic) - 1])
			print("\nGet ready to play Hangman!")
			start_game(word)
		elif urChoice == "2":
			sys.exit()
		else:
			print("Not an option, try again!")
			operator()	 
	

def playAgain():  
	askUsr = input("Again?(Y/N): ").lower()
	if askUsr == "y":
		operator()
	elif askUsr == "n":
		print("Number of play: ", count_play)
		print("Number of win: ", count_win)
		sys.exit()
	else:
		print("Not an option")
		playAgain()


def start_game(word):
	player_lives = 5
	used_letters =[]
	number_dashes=["_" for i in range(len(word))]
	print(visuals(player_lives))
	print(" ".join(number_dashes))
	while player_lives == player_lives:
		input_letter =input("Player 2, input your letter guess: ")
		os.system("cls")
		if len(input_letter) > 1:
			player_lives-= 1
			print(visuals(player_lives))
			print(input_letter,"is not \'a letter\'!")
			print("Used letters:"," ".join(used_letters))
			print((updated_dashes(word,input_letter,number_dashes,)),'')
		elif input_letter  not in used_letters and input_letter in word:
			print(visuals(player_lives))
			print("Correct,",input_letter,"is in the word!")
			if input_letter not in used_letters:
				used_letters.append(str(input_letter))
			else:
				pass
			print("Used letters:"," ".join(used_letters))
			print((updated_dashes(word,input_letter,number_dashes,)),'')
		elif input_letter not in word :
			player_lives-=1
			print(visuals(player_lives))
			print("Incorrect,",input_letter,"is not in the word")
			if input_letter not in used_letters:
				used_letters.append(str(input_letter))
			else:
				pass
			print("Used letters:"," ".join(used_letters))
			print((updated_dashes(word,input_letter,number_dashes,)),'')
		elif input_letter in used_letters:
			player_lives-=1
			print(visuals(player_lives))
			print("You already guessed",input_letter)
			if input_letter not in used_letters:
				used_letters.append(str(input_letter))
			else:
				pass
			print("Used letters:"," ".join(used_letters))
			print((updated_dashes(word,input_letter,number_dashes,)),'')
		if player_lives == 0:
			you_lose(player_lives,word)
		elif word == "".join(number_dashes):
			you_win(player_lives,word)


def updated_dashes(word,input_letter,number_dashes):
	for i in range(len(word)):
		if input_letter == word[i]:
			number_dashes[i] = input_letter
	return (" ".join(number_dashes))


def you_lose(player_lives,word):
	global count_play
	count_play += 1
	print("The guesser loses!","The word was",word)
	playAgain()
	return count_play


def you_win(player_lives,word):
	global count_play
	count_play += 1
	global count_win
	count_win += 1
	print("The guesser wins!","The word was",word)
	playAgain()


def visuals(player_lives):
	if player_lives == 5:
		return"""
		_______
		|     |
		|     
		|
		|
		|
		|
		|________
		|        |
		"""
	elif player_lives == 4:
		return"""
		_______
		|     |
		|     O
		|     |
		|
		|
		|
		|________
		|        |
		"""
	elif player_lives == 3:
		return"""
		_______
		|     |
		|     O
		|    /|\ 
		|
		|
		|
		|________
		|        |
		"""
	elif player_lives == 2:
		return"""
		_______
		|     |
		|     O
		|    /|\ 
		|    / \ 
		|    
		|
		|________
		|        |
		"""
	elif player_lives == 1:
		return"""
		_______
		|     |
		|     l0
		|    |||
		|     |
		|    | |
		|
		|________
		"""
	elif player_lives == 0:
		return"""
⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆
⠀⠀⠀⠀⠹.⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟
		"""	
operator()
