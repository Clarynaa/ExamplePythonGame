import random

class Rat:
    name = "Rat"
    hp = 0
    xp = 0
    damage = 0
    level = 0
    alive = 0

    def __init__(self):
        self.hp = random.randrange(5, 11)
        self.xp = self.hp * 5
        self.damage = random.randrange(1, 2)
        self.level = 1
        self.alive = 1


class Knight:
    maxhp = 30
    hp = 30
    xp = 0
    damage = 3
    level = 1


class Paladin:
    maxhp = 25
    hp = 25
    xp = 0
    damage = 2
    level = 1


class Mage:
    maxhp = 15
    hp = 15
    xp = 0
    damage = 1
    level = 1


class Berserker:
    maxhp = 30
    hp = 30
    xp = 0
    damage = 4
    level = 1


currentScreen = "CharacterCreation"
charName = input("Please enter your character's name: \n")
charGender = input("Please enter your character's gender: \n")
characterClass = ""
player = ""
enemy = ""



def chooseCharacter():
    global characterClass
    global player
    charClass = input("Choose a class: \nKnight\nPaladin\nMage\n"
                      "or type 'INFO classname' for more information on classes\n")

    if charClass.casefold() == "info knight":
        print("The knight is a warrior with a shield.  They do moderate damage and can block to reduce incoming damage\n\n"
              "Starting stats:\nHP: 30\nDamage: 3\n\n"
              "Skills:\nShield Block: Blocks incoming damage while auto-attacking, reducing damage taken by 1\n\n")
        chooseCharacter()

    if charClass.casefold() == "info paladin":
        print("The paladin is a warrior with holy magic.  They can deal decent damage and heal themselves.\n\n"
              "Starting stats:\nHP: 25\nDamage: 2\n\n"
              "Skills: \n Heal: Restores your health by 4\n\n")
        chooseCharacter()

    if charClass.casefold() == "info mage":
        print("The mage is a studious warrior that can cast elemental spells."
              "  They do very little physical damage, but have spells to rely upon.\n\n"
              "Starting stats:\nHP: 15'n Damage: 1\n\n"
              "Skills:\nPyroball: Shoots a ball of flame at a foe.  Does 5 damage\n"
              "Ice Spear: Launches a spear of ice at a foe.  Does 4 damage\n"
              "Earth Spike: Stabs the enemy with a an earthen spike.  Does 5 damage\n\n")
        chooseCharacter()

    if charClass.casefold() == "knight":
        characterClass = "knight"
        player = Knight()

    if charClass.casefold() == "paladin":
        characterClass = "paladin"
        player = Paladin()

    if charClass.casefold() == "mage":
        characterClass = "mage"
        player = Mage()


def startGame():
    global charGender
    if charGender.casefold() == "female":
        print("\nInsert lore stuff about this girl and why she's adventuring\n")
    elif charGender.casefold() == "male":
        print("\nInsert lore stuff about this boy and why he's adventuring\n")
    else:
        print("\nInsert lore about this person and why they're adventuring\n")
    battle()


def battle():
    global player
    global currentScreen
    global enemy
#if player.level == 1:
    enemy = Rat()
    print("You encounter a rat!\n")
    print("What do you want to do?\n")
    currentScreen = "Battle"


def adventure():
    global player
    global currentScreen
    player.hp = player.maxhp
    currentScreen = "Adventure"
    ran = random.randrange(1, 3)
    if ran == 1:
        print("First scenario")
        battle()
    elif ran == 2:
        print("second scenario")
        battle()



def combat():
    global player
    global enemy
    global currentScreen
    turn = input("What do you do?\n Attack \n Flee\n Special\n")
    if turn.casefold() == "attack":
        print("You attack the {} for {} damage\n".format(enemy.name, player.damage))
        enemy.hp -= player.damage
        if enemy.hp > 0:
            print("The {} attacks back for {} damage\n".format(enemy.name, enemy.damage))
            player.hp -= enemy.damage
            print("You have {} hp left\n".format(player.hp))
            combat()
        else:
            print("You killed the {} and gained {} xp!\n"
                  "current xp: {}".format(enemy.name, enemy.xp, player.xp))
            player.xp += enemy.xp
            adventure()
    if turn.casefold() == "flee":
        adventure()


chooseCharacter()
#Debug: Make sure class is chosen correctly
print(characterClass)



currentScreen = "Start"
startGame()

while currentScreen == "Battle":
    combat()






