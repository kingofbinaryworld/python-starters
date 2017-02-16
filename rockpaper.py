import time
import random

rock=1
paper=2
scissors=3

names={rock:"rock",paper:"paper",scissors:"scissors"}		#used to display what computer threw
rules={rock:scissors,paper:rock,scissors:paper}				#used to determine winner rules[player]==computer means player won

player_score=0												#player score tally
computer_score=0											#computer score tally

def start():												#start function continues till game returns a value
	print "Lets play a game of rock paper scissors..."
	while game():											#game returns value of play_again()
		pass
	scores()												#before exiting, score tally is shown

def game():
	player=move()											#player stores the move of user in integer value
	computer=random.randint(1,3)							#randint function used to randomise in range 1 to 3
	result(player,computer)									#result is determined and score tally is updated in the function
	return play_again()									   #asks user whether you wanna play again and then returns it to start

def move():
	while True:													#indefinite loop until player move is returned
		player=raw_input("Enter Rock:1 paper:2 scissors:3")		#takes input from user
		try:
			player=int(player)									#converts from str to int
			if player in (1,2,3):								#if in the range returns the value
				return player
		except ValueError:
			pass
		print "Enter integer"

def result(player,computer):
	print "1.."
	time.sleep(1)												# 1 second delay
	print "2.."
	time.sleep(1)
	print "3!"
	time.sleep(0.5)
	print "Computer threw "+names[computer]						#uses list to know the string name..computer is integer
	global player_score,computer_score							#global used so that we can make change to those variables 
	if player==computer:
		print "Game Tied"
	elif rules[player]==computer:								#Logic..rules[1]==3 means rock-scissor and player wins
		print "You won..."
		player_score+=1											#Score update
	else:
		print "Computer won..hehe"
		computer_score+=1

def play_again():
	play=raw_input("Do you wanna play?")
	if play in ("y","Y","Yes","yes"):
		return play
	else:
		print "Thanks for playing..come again"

def scores():
		print "SCORE TALLY"
		print "Player:",player_score					#we can use global here but it aint necessary
		print "Computer:",computer_score				#as we do not make change to their variables

if __name__== '__main__':					# start() only gets executed when we run this file...it is done so that
	start()									# we can import this file and the game doesnt start by itself
