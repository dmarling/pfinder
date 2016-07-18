from race_info import RACE_DICTIONARY as RD
from class_info import CLASS_DICTIONARY as CD
from class_info import CLASS_SKILLS as CS
from skills import SKILL_RANKS as SR
from ability_score_modifier_info import ability_score_dictionary as ASD
from level_up import spend_ranks
import dice_roll as dice
from dice_roll import print_slow as ps
import shelve, pprint

def check_existing_save():
    """takes no arguments, returns a list of savefiles"""
    gamesave = shelve.open('gamefile')
    ps('Welcome\n')

    for x in list(gamesave.keys()):
    	print(x)

    name=input("To use an existing save [type name], otherwise hit enter\n")
    if name in gamesave.keys():
        return(gamesave[name])
    else:
        print("Begin your new save by creating a character\n")
        player = Initialize_Player()
        gamesave[player.name] = player
        return(player)


class Initialize_Player(object):

	def __init__(self):
		self.level = 1
		self.name = self.char_name()
		self.ability_score = self.generate_ability_score()
		self.inventory = {"wooden sword":1, "rusty helmet":1, "gold":100}
		self.health = 30
		self.character = 'player'
		self.actions = 2
		self.movement = 30
		self.char_class = self.char_class_select()
		self.class_dict = CD[self.char_class]
		self.playerclass = str(self.char_class)
		self.char_race = self.char_race_select()
		self.race_dict = RD[self.char_race]
		self.playerrace = str(self.char_race)
		self.modify_ability_score_class_bonus()
		self.ability_bonus = self.create_skill_modifiers()
		self.ranks = self.get_ranks()
		self.skills = {'ACROBATICS':0, 'APPRAISE':0, 'BLUFF':0, 'CLIMB':0, 'CRAFT':0, 'DIPLOMACY':0,
			'DISABLE DEVICE':0, 'DISGUISE':0, 'ESCAPE ARTIST':0, 'FLY':0, 'HANDLE ANIMAL':0, 'HEAL':0, 'INTIMIDATE':0,
			'ARCANA':0, 'DUNGEONEERING':0, 'ENGINEERING':0, 'GEOGRAPHY':0, 'HISTORY':0, 'LOCAL':0, 'NATURE':0, 'NOBILITY':0,
			'PLANES':0, 'RELIGION':0, 'LINGUISTICS':0, 'PERCEPTION':0, 'PERFORM':0,
			'PROFESSION':0, 'RIDE':0, 'SENSE MOTIVE':0, 'SLEIGHT OF HAND':0, 'SPELLCRAFT':0, 'STEALTH':0, 'SURVIVAL':0,
			'SWIM':0,'USE MAGIC DEVICE':0}
		self.choose_player_skills()
		spend_ranks(self)

	def char_name(self):
		"""takes no arguments, returns a string"""

		player_name = input('Name your character \n')
		player_name = str(player_name)
		return(player_name)

	def generate_ability_score(self):
		"""takes no arguments, returns a dict
		   will be used in the character class"""

		while True:
			rolls=[]
			for x in range(0,6):
			   rolls.append(dice.rollit(3,6))
			print('\n')
			print(rolls)
			if sum(rolls) > 60:
				break
			else:
				response=input('Ouch! Would you like a reroll? (Y/N)\n')
				if response.upper()=='Y':
					continue
				else:
					break
		print('\nFrom the above list, choose a value for each Attribute when prompted...\n')
		attributes=['DEXTERITY','STRENGTH','CONSTITUTION','INTELLIGENCE','WISDOM','CHARISMA']
		ability_score={}
		for x in range(0,len(attributes)):
			while True:
				response=int(input('Choose your %s\n' %attributes[x]))
				if response in rolls:
					ability_score[attributes[x]]=response
					rolls.remove(response)
					break
				else:
					print('that value is not available\n')
		return(ability_score)

	def char_class_select(self):
		"""takes no arguments, returns a string
		   will be used in the character class"""

		selection=''
		valid_answers=['BARBARIAN', 'BARD', 'CLERIC', 'DRUID', 'FIGHTER', 'MONK', 'PALADIN', 'RANGER', 'ROGUE', 'SORCERER', 'WIZARD', 'READY']
		while True:
			race=input("Please select a class to learn more...\n ('Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Wizard')\nOr if you are ready to choose type 'ready'\n")
			race=race.upper()
			if race =='READY':
				break
			elif race in valid_answers:
				selection=race
				print('\n')
				pprint.pprint(CD[selection])
				print('\n')
			else:
				print('please try again')
		while True:
			choice=input("Choose your class ('Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Wizard') \n")
			choice=choice.upper()
			if choice not in valid_answers:
				print("That doesn't appear to be a valid class")
			else:
				print('you have chosen %s' %choice)
				return(choice)

	def char_race_select(self):
		"""takes no arguments, returns a string"""
		valid_answers=['DWARF', 'ELF', 'GNOME', 'HALF-ELF', 'HALF-ORC', 'HALFLING', 'HUMAN', 'READY']
		while True:
			race=input("Please select a race to learn more...\n (Dwarf, Elf, Gnome, Half-Elf, Half-Orc, Halfling, Human)\nOr if you are ready to choose type 'ready'\n")
			race=race.upper()
			selection=race
			if race =='READY':
				break
			elif race in valid_answers:
				print( RD[selection]['GENERAL DESCRIPTION'] )
				for x in ('SOCIETY','RELATIONS','ALIGNMENT AND RELIGION','ADVENTURERS'):
					response=input(" <'More details please!' [press 1] or 'I've seen enough!' [press 2]>\n")
					if response=='1':
						print(RD[selection][x])
						print('\n')
					else:
						for x in (RD[selection]['RACIAL TRAITS'].keys()):
							response=input("<'Show me some stats!' [press 1] or 'I've seen enough!' [press 2]>\n")
							if response=='1':
								print(RD[selection]['RACIAL TRAITS'][x])
							else:
								break
						break
		while True:
			choice=input("Choose your race (Dwarf, Elf, Gnome, Half-Elf, Half-Orc, Halfling, Human) \n")
			choice=choice.upper()
			if choice not in valid_answers:
				print("That doesn't appear to be a valid race")
			else:
				print('you have chosen %s' %choice)
				return(choice)

	def modify_ability_score_class_bonus(self):
		""" returns dict player_ability_score """
		attributes=['WISDOM','INTELLIGENCE','STRENGTH','CHARISMA','CONSTITUTION','DEXTERITY']
		racial_ability_bonus={}
		if self.playerrace in ['HALF-ORC','HALF-ELF','HUMAN']:
			while True:
				ability=input('Please select an attribute from the following to recieve a +2 bonus\nWisdom,Intelligence,Strength,Charisma,Constitution,Dexterity\n')
				ability=ability.upper()
				if ability in attributes:
					racial_ability_bonus[ability]=2
					attributes.remove(ability)
					for x in attributes:
						racial_ability_bonus[x]=0
					break
		else:
			racial_ability_bonus=RD[self.playerrace]['RACIAL_ABILITY_BONUS']
		for attr in self.ability_score.keys():
			if attr in racial_ability_bonus.keys():
				self.ability_score[attr]=racial_ability_bonus[attr]+self.ability_score[attr]
		return(self.ability_score)

	def get_ranks(self):
		class_ranks=0
		if self.playerrace == 'HUMAN':
			class_ranks+=1
		class_ranks+=self.ability_bonus['INTELLIGENCE']
		class_ranks+=SR[self.playerclass]
		if class_ranks <= 0:
			class_ranks = 1
		return class_ranks

	def create_skill_modifiers(self):
		ability_bonus={'WISDOM':0,'INTELLIGENCE':0,'STRENGTH':0,'CHARISMA':0,'CONSTITUTION':0,'DEXTERITY':0}
		for x in self.ability_score.keys():
			ability_bonus[x]=ASD[str(self.ability_score[x])]
		return(ability_bonus)

	def choose_player_skills(self):
		ps("From your allotted %d skillranks choose skills\n" %self.ranks)
		for skill in self.skills.keys():
			print(skill)
		input("\nPress 'Enter' to continue...\n")
		print('''Level 1 costs 1 skill rank, Level 2 costs 2 skill ranks and so forth.\n You may not have any skill with a greater level than your player level\n''')
		ps('The following skills recieve natural bonuses for yoru class\n')
		for skill in CS[self.playerclass].keys():
			if CS[self.playerclass][skill] == 1:
				print(skill)
		input("\nPress 'Enter' to continue...\n")

	def stomp(self, target):
		dmg =  dice.rollit(2,5)
		target.health -= dmg
		return(dmg)

class initialize_monster(object):

	def __init__(self, name):
		self.level = 1
		self.name = name
		self.inventory = {"wooden sword":1, "rusty helmet":1, "gold":100}
		self.health = 10
		self.actions = 2
		self.movement = 20
		self.character = 'monster'

	def claw(self, target):
		dmg =  dice.silentroll(2,3)
		target.health -= dmg
		return(dmg)
			

###########################################################################
###########################################################################
###########################################################################
###########################################################################

player=check_existing_save()
print(player.ability_score)
print(player.ranks)
#ps("that's all so far, wasn't it fun\n")

ps('suddenly...\n a vampire!\n')
from action_turn import role_turn, check_health, engage
vampire=initialize_monster('vampire')
myword=role_turn([vampire,player])


#for x in myword:
#	print( check_health(x[2]) )

engage(myword,player,vampire)

#total_enemy_health = 1
#while total_enemy_health > 0:
#	for x in myword:
#		for y in range(0,int(x[2].actions)):
#			input('{1} performs action {0}\n'.format(y,x[0]))
#	total_enemy_health=0
#	for x in myword:
#	#	print(x[2].health)
#	#	print(x[2].actions)
#		if x[0] !='player':
#			total_enemy_health+=x[2].health
			
#print(myword)



#while (sum of all enemy health > 0 or sum of player health < 0):
		
#def start_order(player_list):
			
