from dice_roll import rollit,silentroll

def role_turn(persons):
	'''takes a list of players/monster objects and returns the turnorder'''
	turnorder=[]
	for x in persons:
		#roll for intiative here
		if x.character == 'player':
			rollval=rollit(1,20)	
		elif x.character == 'monster':
			rollval=silentroll(1,15)
		else:
			raise RuntimeError('no type listed for initiative roll')	
		turnorder.append((x.name,rollval, x))
	turnorder.sort(key=lambda turnorder: turnorder[0], reverse=True)
	return(turnorder)

def check_health(char):
	if char.health > 0:
		return(True)
	else:
		return(False)

def engage(char_list,player, vampire):
	ans=input('Do you engage?\n')
	if ans.lower() == 'yes':
		
		total_enemy_health = 1
		while total_enemy_health > 0:
			if allpcs(char_list,player,vampire) == 0:
				print('player has died')
				break
			elif allpcs(char_list,player,vampire) == 1:
				print('monster has died')
				break
			else:
				pass

		#	if check_health(player) is False:
		#		print('{} has died'.format(player.name))
		#		break
#			for x in char_list:
#				if check_health(player) is False:
#					break
#				print(x[2].health,x[0])
#				for y in range(0,int(x[2].actions)):
#					#print(x[0],y,x)
#					if check_health(player) is False:
#						break
#					if x[2].character == 'monster':
#						damage = x[2].claw(player)
#						print('{1}  does {0} damage'.format(damage,x[0]))
#						input()
#					if x[2].character == 'player':
#						print('player does not react')
#			total_enemy_health=0
#			for x in char_list:
#				if x[2].character != 'player':
#					total_enemy_health+=x[2].health
			

def allpcs(char_list,player,vampire):
	print(char_list)	
	for x in char_list:
		print(x[2].health,x[0])
		for y in range(0,int(x[2].actions)):
			if check_health(player) is False:
				return(0)
			#print(x[0],y,x)
			if check_health(vampire) is False:
				return(1)
			if x[2].character == 'monster':
				damage = x[2].claw(player)
				print('{1}  does {0} damage'.format(damage,x[0]))
				input()
			if x[2].character == 'player':
				yourtarget=input('specify who you are attacking\n')
				damage = x[2].stomp(vampire)
				print('player does not react')
	total_enemy_health=0



def allpcs(char_list):
	print(char_list)	
	persons=[]
	for x in char_list:
		persons.append(x[2])
		#print(x[2].health,x[0])
		for y in range(0,int(x[2].actions)):
			if check_health(player) is False:
				return(0)
			#print(x[0],y,x)
			if check_health(vampire) is False:
				return(1)
			if x[2].character == 'monster':
				damage = x[2].claw(player)
				print('{1}  does {0} damage'.format(damage,x[0]))
				input()
			if x[2].character == 'player':
				yourtarget=input('specify who you are attacking\n')
				damage = x[2].stomp(vampire)
				print('player does not react')
	total_enemy_health=0



