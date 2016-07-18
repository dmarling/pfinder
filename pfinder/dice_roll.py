import random
import time

def rollit(quantity,value):
	'''dice roll for players, prompts for
		roll, and displays die values'''
	total=0
	showlist=""
	input("Press any key to roll...")
	for x in range(0,quantity):
		roll=random.randint(1,value)
		showlist+=('['+str(roll)+']')
		total+=roll
	print(showlist)
	return total

def npcroll(quantity,value):
	'''dice roll for npcs, displays die values'''
	total=0
	showlist=""
	for x in range(0,quantity):
		roll=random.randint(1,value)
		showlist+=('['+str(roll)+']')
		total+=roll
	print(showlist)
	return total

def silentroll(quantity,value):
	'''dice roll that returns only the total'''
	total=0
	for x in range(0,quantity):
		roll=random.randint(1,value)
		total+=roll
	return total

def print_slow(mystr):
	for letter in mystr:
		print(letter,end='')
		time.sleep(.05)

