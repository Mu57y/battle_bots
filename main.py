import random 

class Player: 
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attack(self, opponent):
        opponent.health -= self.damage

    def take_damage(self, damage_dealt):
        self.health -= damage_dealt

    def heal(self):
        self.health += 10

    def block(self, opponent):
        opponent.damage = 0

class Game: 

    @staticmethod
    def fight(player, computer):
        round_count = 1

        # I figured it was best to give a limit as to how many times the player and computer can heal:
        player_heal_count = 0
        computer_heal_count = 0 
    
        while player.health > 0 and computer.health > 0:

# This part lays out the avaliable options for the player and the computer based on 
# their health and healing turns

            # if player's health is equal to 100 and their healing turns are below 5
            if player.health == 100 and player_heal_count < 5:

                player_choice = input("Press 1 to attack and 2 to block: ")
                if player_choice == "1":
                    player_action = "attack"
                elif player_choice == "2":
                    player_action = "block"

            # if player's health is less than 100 and their healing turns are below 5
            elif player.health < 100 and player_heal_count < 5:

                player_choice = input("Press 1 to attack, 2 to block, and 3 to heal: ")
                if player_choice == "1":
                    player_action = "attack"
                elif player_choice == "2":
                    player_action = "block"
                elif player_choice == "3":
                    player_action = "heal"

            # if player's healing turns are below 5
            elif player_heal_count < 5: 

                player_choice = input("Press 1 to attack, 2 to block, and 3 to heal: ")
                if player_choice == "1":
                    player_action = "attack"
                elif player_choice == "2":
                    player_action = "block"
                elif player_choice == "3":
                    player_action = "heal"

            # if player's healing turns are above 5
            elif player_heal_count > 5:

                player_choice = input("Press 1 to attack and 2 to block: ")
                if player_choice == "1":
                    player_action = "attack"
                elif player_choice == "2":
                    player_action = "block"

            # if the player's health is 100 
            elif player.health == 100:

                player_choice = input("Press 1 to attack and 2 to block: ")
                if player_choice == "1":
                    player_action = "attack"
                elif player_choice == "2":
                    player_action = "block"


            computer_choice = random.randint(0, 100)

            # if computer's health is equal to 100 and its healing turns are below 5
            if computer.health == 100 and computer_heal_count < 5: 

                if computer_choice > 0 and computer_choice < 50:
                    computer_action = "attack"
                elif computer_choice > 50 and computer_choice < 100:
                    computer_action = "block" 

            # if computer's health is less than 100 and its healing turns are below 5
            elif computer.health < 100 and computer_heal_count < 5: 

                if computer_choice > 0 and computer_choice < 30:
                    computer_action = "attack"
                elif computer_choice > 30 and computer_choice < 60:
                    computer_action = "block" 
                elif computer_choice > 60 and computer_choice < 90:
                    computer_action = "heal"

            # if player's healing turns are below 5
            elif computer_heal_count < 5:

                if computer_choice > 0 and computer_choice < 30:
                    computer_action = "attack"
                elif computer_choice > 30 and computer_choice < 60:
                    computer_action = "block" 
                elif computer_choice > 60 and computer_choice < 90:
                    computer_action = "heal"

            # if player's healing turns are above 5
            elif computer_heal_count > 5: 

                if computer_choice > 0 and computer_choice < 50:
                    computer_action = "attack"
                elif computer_choice > 50 and computer_choice < 100:
                    computer_action = "block" 

            # if the player's health is 100 
            elif computer.health == 100:

                if computer_choice > 0 and computer_choice < 50:
                    computer_action = "attack"
                elif computer_choice > 50 and computer_choice < 100:
                    computer_action = "block" 

# Some of the if statements that just called in the functions from the Player class that conflicted with one 
# another (i.e. player attacks and computer blocks) required cancelling some of the if statements. So I simply
# wrote a whole list of possible conflicting scenarios and coded specific instructions for those situations. 

            # if the player is attacking and the computer is attacking
            if player_action == "attack" and computer_action == "attack":
                player.health -= 10
                computer.health -= 10

            # if the playeris blocking and the computer is blocking
            elif player_action == "block" and computer_action == "block":          
                player.block(computer)
                computer.block(player)

            # if the player is attacking and the computer is blocking 
            elif player_action == "attack" and computer_action == "block":
                computer.block(player)

            # if the player is blocking and the computer is attacking
            elif player_action == "block" and computer_action == "attack":
                player.block(computer)

            # if the player is attacking and the computer is healing 
            elif player_action == "attack" and computer_action == "heal":
                computer.health += 10
                computer_heal_count += 1 

            # if the player is healing and the computer is attacking
            elif player_action == "heal" and computer_action == "attack":
                player.health += 10
                player_heal_count += 1

            # if both the player and computer are healing
            elif player_action == "heal" and computer_action == "heal":
                player.health += 10
                computer.health += 10
                player_heal_count += 1
                computer_heal_count += 1

            # if the player is healing
            elif player_action == "heal":
                player.heal()
                player_heal_count += 1
            
            # if the computer is healing
            elif computer_action == "heal":
                computer.heal()
                computer_heal_count += 1 

            # if the player heals more than 5 times
            elif player_heal_count == 5:
                print("Sorry, you ran out of healing turns!")
            
            # if the computer heals more than 5 times
            elif computer_heal_count == 5:
                print("The computer ran out of healing turns!")

            # what to print at the end of each round, once both the player 
            # and the computer have taken their moves
            print("\n---------------------")
            print("Round: " + str(round_count))
            print("Your healing turns: " + str(player_heal_count))
            print("Opponenet healing turns: " + str(computer_heal_count))
            print("")
            print("  Your action: " + player_action)
            print("  Opponent action: " + computer_action)
            print("  Your health: " + str(player.health))
            print("  Opponent health: " + str(computer.health))
            print("---------------------")

            # if the player's health is equal to or below 0, they loose
            if player.health <= 0:
                print("") 
                print("You lose!")
                print("")

            # if the computer's health is equal to or below 0, you win 
            if computer.health <= 0:
                print("You win!")
                print("")

            round_count += 1

# calling the functions: 
user = Player("Player")
computer = Player("Computer")

Game.fight(user, computer)
