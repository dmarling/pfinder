def spend_ranks(player):
	ranks_available = player.ranks
	while ranks_available > 0:
		print("you have %d ranks to use...\n" %ranks_available)
		ans=input('''Would you like to spend ranks on skills (y/n)\n''')
		if ans.upper() == 'N':
			break
		else:
			for skill in player.skills.keys():
				print(skill) 
			selection=input('Choose from the following skills\n')				
			selection=selection.upper()
			player.skills[selection]+=1
			ranks_available-=player.skills[selection]

def earn_ranks(player):
	pass

def health_bonus(player):
	pass


