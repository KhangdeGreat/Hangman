import os
import sys
import random

word = ""
player_lives = 5
askUsr = ""
count_play = 0
count_win = 0
topic = [
	["car", "caro", "carole"],
	["dog", "doga", "dogalo"],
	["apple", "appleni", "applenol"],
	["hot", "cold", "coldest"]
]


def topic1(usrTopic):
	if usrTopic == 1:
		os.system("cls")
		print("The topic is: Cars")
		return topic[usrTopic - 1]
	elif usrTopic == 2:
		os.system("cls")
		print("The topic is: Dogss")
		return topic[usrTopic - 1]
	elif usrTopic == 3:
		os.system("cls")
		print("The topic is: Appless")
		return topic[usrTopic - 1]
	elif usrTopic == 4:
		os.system("cls")
		print("The topic is: Weather")
		return topic[usrTopic - 1]
	else:
		recast()

print("1. Play\n2. Exit")
urChoice = input("Option: ")

      
def recast():	
	while True:
		if urChoice == 1:
			os.system("cls")
			usrTopic = 0
			usrTopic = int(input("\nPlayer 1 enter topic number(1-4): "))
			topic1(usrTopic)
			word = random.choice(topic[usrTopic - 1])
			print("\nGet ready to play Hangman!")
			start_game(word)
		elif urChoice == 2:
			sys.exit()
		else:
			print("Not an option!, try agian. ")
			recast()

def playAgain():  
	askUsr = input("Again?(Y/N): ").lower()
	# while askUsr == "y" or askUsr == "n":
	if askUsr == "y":
		recast()
	elif askUsr == "n":
		print("Number of win:\n ", count_win)
		print("")
		print("Number of play:\n ", count_play)
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
recast()