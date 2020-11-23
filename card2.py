from random import randint, choice

def jack_chooses_a_card(suits: dict):
    """
    Program for Card Game
    """
    print(str(randint(1,13)) + " of " + str(choice(suits)))
def check_help():
    # Instructions for the help
    multiline_str = """Welcome to Pick a Card Game.
    To play the game, follow the instruction below.
    1. Enter your name at the begining of the program.
    2. press Enter to continue...
    3. Pick a Card."""
    print("Game Instruction: \n" + multiline_str)
   
if __name__ == "__main__":

    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    player_name= input(str("Enter your name: " ))
    print("It's "+player_name+"'s turn")
    print("Just press [ENTER] to get started")
  
    user_input = input("")
    if(user_input == '--help'):
        check_help()
        
        
print("Just type [--resume] to Resume the Game")
    
while user_input == "":
    jack_chooses_a_card(suits)
    user_input = input("\nTo run again press [ENTER] key, entering anything else would terminate the program\n")