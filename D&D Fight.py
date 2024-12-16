import random


monsterRollD6 = 0
monsterRollD20 = 0
playerRollD6 = 0
playerRollD20 = 0

def rollD20(): 
    D20Roll = random.randint(1, 20)

    return D20Roll

def rollD4():
    D4Roll = random.randint(1, 4)

    return D4Roll

def rollD6():
    D6Roll = random.randint(1, 6)

    return D6Roll

def rollD8():
    D8Roll = random.randint(1, 8)

    return D8Roll

def stats():
   
    Str = 0
    Int = 0
    Wis = 0
    Dex = 0
    Con = 0
    Cha = 0

    Str = rollD20()
    Int = rollD20()
    Wis = rollD20()
    Dex = rollD20()
    Con = rollD20()
    Cha = rollD20()

    return Str, Int, Wis, Dex, Con, Cha

    


def main():

    monsterHealth = 10
    playerHealth = 10
    monsterAC = 6
    playerAC = 5
    playerStats = stats()
    

    print("Welcome to a mini D&D fight simulator. \n"
          "We are going to simulate a D&D fight, fighting only 1 Monster.\n")
    
    input("We are going to roll for your stats.\n"
          "There will be Strength, Intelligence, Wisdom, Dexterity, Constitution, and Charisma. These won't be important for now. Please hit enter to continue.")
    
    
    print(playerStats)

    input("\nGreat! Now that we have your stats we can do a quick monster fight to get you prepared for real battles.\n")

    input("A goblin appears in front of you armed with a dagger and leather armor. They have an armor class of " + str(monsterAC) + "\n"
          "You will be armed with a sword and chain mail armor. You have an armor class of " + str(playerAC))
    
    print("Both of you have 10 health.")
    
    while monsterHealth > 0 and playerHealth > 0:

        print("\nThe Goblin has " + str(monsterHealth) + " Hitpoints remaining.")
        print("You have " + str(playerHealth) + " Hitpoints remaining. \n")
        input("We will roll for Initiative.")
        
        monsterRollD6 = rollD6()
        playerRollD6 = rollD6()
        print("You have rolled a " + str(playerRollD6))

        if (monsterRollD6 > playerRollD6):
            print("The Goblin won the initiative, they will attack first.")
            input("The Goblin lunges towards you with their dagger.")
            monsterRollD20 = rollD20()
            if (monsterRollD20 >= 14):
                hit = rollD4()
                input("The Golbin's dagger hits its mark. \n"
                    "He hits you for " + str(hit) + " points of damage.")
                playerHealth = playerHealth - hit
                input("It is now your turn to attack.")
                input("You surge forward with your sword.")
                playerRollD20 = rollD20()
                if (playerRollD20 >= 13):
                    hit = rollD8()
                    input("Your attack hit! You hit the goblin for " + str(hit) + " points of damage")
                    monsterHealth = monsterHealth - hit
                else: 
                    input("Your attack missed. The Goblin takes no damage.")
            else:
                input("The Golbin's hit missed! It is your turn to attack.")
                input("You surge forward with your sword.")
                playerRollD20 = rollD20()
                if (playerRollD20 >= 13):
                    hit = rollD8()
                    input("Your attack hit! You hit the goblin for " + str(hit) + " points of damage")
                    monsterHealth = monsterHealth - hit
                else: 
                    input("Your attack missed. The Goblin takes no damage.")

        elif (playerRollD6 > monsterRollD6):
            print("You have won initiative, you will attack first.")
            input("You surge forward with your sword.")
            playerRollD20 = rollD20()
            if (playerRollD20 >= 13):
                hit = rollD8()
                input("Your attack hit! You hit the goblin for " + str(hit) + " points of damage")
                monsterHealth = monsterHealth - hit
                input("It is the Goblins turn to attack.")
                input("The goblin lunges towards you with their dagger.")
                monsterRollD20 = rollD20()
                if (monsterRollD20 >= 14):
                    hit = rollD4()
                    input("The Golbin's dagger hits its mark. \n"
                        "He hits you for " + str(hit) + " points of damage.")
                    playerHealth = playerHealth - hit
                else: 
                    input("The Golbin's hit missed! You take no damage.")
            else: 
                input("Your attack missed. The Goblin takes no damage.")
                input("It is the Goblins turn to attack.")
                input("The goblin lunges towards you with their dagger.")
                monsterRollD20 = rollD20()
                if (monsterRollD20 >= 14):
                    hit = rollD4()
                    input("The Golbin's dagger hits its mark. \n"
                        "He hits you for " + str(hit) + " points of damage.")
                    playerHealth = playerHealth - hit
                else:
                    input("The Golbin's hit missed! You take no damage.")
                
        else: 
            input("You have tied, attacks will happen simultaneously.")
            input("You and the Goblin lunge forward at once.")
            playerRollD20 = rollD20()
            if (playerRollD20 >= 13):
                hit = rollD8()
                print("Your attack hit! You hit the goblin for " + str(hit) + " points of damage")
                monsterHealth = monsterHealth - hit
                monsterRollD20 = rollD20()
                if (monsterRollD20 >= 14):
                    hit = rollD4()
                    input("The Golbin's dagger hits its mark. \n"
                        "He hits you for " + str(hit) + " points of damage.")
                    playerHealth = playerHealth - hit
                else: 
                    input("The Golbin's hit missed! You take no damage.")
            else: 
                print("Your attack missed. The Goblin takes no damage.")
                monsterRollD20 = rollD20()
                if (monsterRollD20 >= 14):
                    hit = rollD4()
                    input("The Golbin's dagger hits its mark. \n"
                        "He hits you for " + str(hit) + " points of damage.")
                    playerHealth = playerHealth - hit
                else:
                    input("The Golbin's hit missed! You take no damage.")


    if (playerHealth == 0 and monsterHealth != 0):

        input("You have fallen unconcious and the Goblin has won. ")

    elif (monsterHealth == 0 and playerHealth != 0):

        input("You have defeated the Goblin. You may continue your adventure.")

    else: 

        input("You have both fallen unconcious, no one has won this battle.")




main()
