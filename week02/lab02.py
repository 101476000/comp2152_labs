# Import the random library to use for the dice later
import random

# Define Variables
numLives = 10           # number of player's lives remaining
mNumLives = 12          # number of monster's lives remaining

diceOptions = [1, 2, 3, 4, 5, 6]
combatStrength = int(input("Enter your combat Strength: "))
mCombatStrength = int(input("Enter the monster's combat Strength: "))

input("Roll the dice for your health points (Press enter)")
healthPoints = random.choice(diceOptions)
print("You rolled " + str(healthPoints) + " health points")

input("Roll the dice for the monster's health points (Press enter)")
mHealthPoints = random.choice(diceOptions)
print("You rolled " + str(mHealthPoints) + " health points for the monster")

input("Roll the dice to see if you find a healing potion (Press enter)")
healingPotion = random.choice([0, 1])
print("Have you found a healing potion?: " + str(bool(healingPotion)))

input("Analyze the roll (Press enter)")
# Equality operators
print("--- You are matched in strength: " + str(combatStrength == mCombatStrength))

# Relational operators
print("--- You have a strong player: " + str((combatStrength + healthPoints) >= 15))

# and keyword
print("--- Remember to take a healing potion!: " + str(healingPotion == 1 and healthPoints <= 6))

# not keyword
print("--- Phew, you have a healing potion: " + str(
    not (                               # monster will NOT kill hero in one blow
        healthPoints < mCombatStrength  # monster will kill hero in one blow
    )
    and
    healingPotion == 1                  # hero has a healing potion
))

# or keyword
print("--- Things are getting dangerous: " + str(healingPotion == 0 or healthPoints == 1))

# in keyword
print("--- Is it possible to roll 0 in the dice?: " + str(0 in diceOptions))

# --- Expanded if statement
if healthPoints >= 5:
    print("--- Your health is ok")
elif healingPotion == 1:
    healingPotion = 0
    healthPoints = 6
    print("--- Using your healing potion... Your Health Points is now full at " + str(healthPoints))
else:
    print("--- Your health is low at " + str(healthPoints) + " and you have no healing potions available!")


# --- Nested if statement
print("You meet the monster. FIGHT!!")
input("You strike first (Press enter)")

print("Your sword (" + str(combatStrength) + ") ---> Monster (" + str(mHealthPoints) + ")")
if combatStrength >= mHealthPoints:
    mHealthPoints = 0
    print("You've killed the monster")
else:
    mHealthPoints -= combatStrength

    print("You've reduced the monster's health to: " + str(mHealthPoints))

    print("The monster strikes!!!")
    print("Monster's Claw (" + str(mCombatStrength) + ") ---> You (" + str(healthPoints) + ")")
    if mCombatStrength >= healthPoints:
        healthPoints = 0
        print("You're dead")
    else:
        healthPoints -= mCombatStrength
        print("The monster has reduced your health to: " + str(healthPoints))

#Coding Questions

# 1: Define a new array called weapons and add 6 different weapon names
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# 2: Roll the dice (1-6) to choose which weapon you must use
weapon_roll = input("Roll the dice (enter a number between 1 and 6): ")

# 3: Save the roll in a variable called weaponRoll
if not weapon_roll.isdigit():  # Check if input is a number
    print("Invalid input! Please enter a number between 1 and 6.")
else:
    weapon_roll = int(weapon_roll)  # Convert input to integer
    if weapon_roll < 1 or weapon_roll > 6:  # Check if input is within range
        print("Invalid input! Please enter a number between 1 and 6.")
    else:
        weaponRoll = weapon_roll  # Save the roll in weaponRoll

        # 4: Add your weaponRoll to the hero's combat strength
        combatStrength = 0  # Initialize combat strength
        combatStrength += weaponRoll  # Add weaponRoll to combatStrength

        # 5: Use weaponRoll as an index into the weapons array and print the weapon name
        hero_weapon = weapons[weaponRoll - 1]  # Subtract 1 for zero-based indexing
        print(f"You rolled: {hero_weapon}")

        # 6: Define the following conditions
        # 6a: If weaponRoll is less than or equal to 2
        if weaponRoll <= 2:
            print("You rolled a weak weapon, friend.")
        # 6b: But if weaponRoll is less than or equal to 4
        elif weaponRoll <= 4:
            print("Your weapon is meh.")
        # 6c: Else
        else:
            print("Nice weapon, friend!")

        # 6d: If the weapon rolled is not a Fist
        if hero_weapon != "Fist":
            print("Thank goodness you didn't roll the Fist...")

        # 7: Add error handling on all inputs using conditional if statements
        # (This step is already implemented above)