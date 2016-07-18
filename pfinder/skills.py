SKILL_RANKS= {'BARBARIAN':4, 'BARD':6, 'CLERIC':2, 'DRUID':4, 'FIGHTER':2, 'MONK':	4, 'PALADIN':2, 'RANGER':6, 'ROGUE':8, 'SORCERER':2, 'WIZARD':2}

'''
add int modifier to above scores
Humans gain 1 additional skill rank per class level.
all gain 1 additional skill rank or an additional hit point on lvl up.
Each skill rank grants a +1 bonus on checks made using that skill.
'''


'''
When you make a skill check, you roll 1d20 and then add your ranks and the appropriate ability score modifier to the result of this check.
If the skill you're using is a class skill (and you have invested ranks into that skill), you gain a +3 bonus on the check. If you are not trained in the skill (and if the skill may be used untrained),
you may still attempt the skill, but you use only the bonus (or penalty) provided by the associated ability score modifier to modify the check.
Skills can be further modified by a wide variety of sources by your race, by a class ability, by equipment, by spell effects or magic items, and so on.'

Table: Skill Check Bonuses
Skill	Skill Check is Equal To*
Untrained	1d20 + ability modifier + racial modifier
Trained	1d20 + skill ranks + ability modifier + racial modifier
Trained Class Skill	1d20 + skill ranks + ability modifier + racial modifier + 3
* Armor check penalty applies to all Strength- and Dexterity-based skill checks.
If the result of your skill check is equal to or greater than the difficulty class (or DC) of the task you are attempting to accomplish
 If it is less than the DC, you fail.

'''

SKILL_CHECKS={'ACROBATICS'        : {'UNTRAINED' : 1,'ABILITY' : 'DEX','ARMOR CHECK' : 1},
 'APPRAISE'         : {'UNTRAINED' : 1,'ABILITY' : 'INT','ARMOR CHECK' : 0},
 'BLUFF'            : {'UNTRAINED' : 1,'ABILITY' : 'CHA','ARMOR CHECK' : 0},
 'CLIMB'            : {'UNTRAINED' : 1,'ABILITY' : 'STR','ARMOR CHECK' : 1},
 'CRAFT'            : {'UNTRAINED' : 1,'ABILITY' : 'INT','ARMOR CHECK' : 0},
 'DIPLOMACY'        : {'UNTRAINED' : 1,'ABILITY' : 'CHA','ARMOR CHECK' : 0},
 'DISABLE DEVICE'   : {'UNTRAINED' : 0,'ABILITY' : 'DEX','ARMOR CHECK' : 1},
 'DISGUISE'         : {'UNTRAINED' : 1,'ABILITY' : 'CHA','ARMOR CHECK' : 0},
 'ESCAPE ARTIST'    : {'UNTRAINED' : 1,'ABILITY' : 'DEX','ARMOR CHECK' : 1},
 'FLY'              : {'UNTRAINED' : 1,'ABILITY' : 'DEX','ARMOR CHECK' : 1},
 'HANDLE ANIMAL'    : {'UNTRAINED' : 0,'ABILITY' : 'CHA','ARMOR CHECK' : 0},
 'HEAL'             : {'UNTRAINED' : 1,'ABILITY' : 'WIS','ARMOR CHECK' : 0},
 'INTIMIDATE'       : {'UNTRAINED' : 1,'ABILITY' : 'CHA','ARMOR CHECK' : 0},
 'ARCANA'           : {'UNTRAINED' : 0,'ABILITY' : 'WIS','ARMOR CHECK' : 0},
 'DUNGEONEERING'    : {'UNTRAINED' : 0,'ABILITY' : 'WIS','ARMOR CHECK' : 0},
 'ENGINEERING'      : {'UNTRAINED' : 0,'ABILITY' : 'WIS','ARMOR CHECK' : 0},
 'GEOGRAPHY'        : {'UNTRAINED' : 0,'ABILITY' : 'WIS','ARMOR CHECK' : 0},
 'HISTORY'          : {'UNTRAINED' : 0,'ABILITY' : 'WIS','ARMOR CHECK' : 0},
 'LOCAL'            : {'UNTRAINED' : 0,'ABILITY' : 'WIS','ARMOR CHECK' : 0},
 'NATURE'           : {'UNTRAINED' : 0,'ABILITY' : 'WIS','ARMOR CHECK' : 0},
 'NOBILITY'         : {'UNTRAINED' : 0,'ABILITY' : 'WIS','ARMOR CHECK' : 0},
 'PLANES'           : {'UNTRAINED' : 0,'ABILITY' : 'WIS','ARMOR CHECK' : 0},
 'RELIGION'         : {'UNTRAINED' : 0,'ABILITY' : 'WIS','ARMOR CHECK' : 0},
 'LINGUISTICS'      : {'UNTRAINED' : 0,'ABILITY' : 'WIS','ARMOR CHECK' : 0},
 'PERCEPTION'       : {'UNTRAINED' : 1,'ABILITY' : 'WIS','ARMOR CHECK' : 0},
 'PERFORM'          : {'UNTRAINED' : 1,'ABILITY' : 'CHA','ARMOR CHECK' : 0},
 'PROFESSION'       : {'UNTRAINED' : 0,'ABILITY' : 'WIS','ARMOR CHECK' : 0},
 'RIDE'             : {'UNTRAINED' : 1,'ABILITY' : 'DEX','ARMOR CHECK' : 1},
 'SENSE MOTIVE'     : {'UNTRAINED' : 1,'ABILITY' : 'WIS','ARMOR CHECK' : 0},
 'SLEIGHT OF HAND'  : {'UNTRAINED' : 0,'ABILITY' : 'DEX','ARMOR CHECK' : 1},
 'SPELLCRAFT'       : {'UNTRAINED' : 0,'ABILITY' : 'INT','ARMOR CHECK' : 0},
 'STEALTH'          : {'UNTRAINED' : 1,'ABILITY' : 'DEX','ARMOR CHECK' : 1},
 'SURVIVAL'         : {'UNTRAINED' : 1,'ABILITY' : 'WIS','ARMOR CHECK' : 0},
 'SWIM'             : {'UNTRAINED' : 1,'ABILITY' : 'STR','ARMOR CHECK' : 1},
 'USE MAGIC DEVICE' : {'UNTRAINED' : 0,'ABILITY' : 'CHA','ARMOR CHECK' : 0}
}

