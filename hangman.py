import turtle
import random

#Function used to build word from guesses
def get_guessed(word, guesses):
  out = ''
  for letter in word:
    if letter in guesses:
      out += letter
    else:
      out += '_'
  return out


# Create turtle and clear screen
screen = turtle.Screen()
t = turtle.Turtle()
screen.clear()

# Generate the word to guess
words = ["cat", "dog", "horse", "cow", "mouse", "lion", "tiger", "snake"]
word = random.choice(words)

# Game Variables
game_over = False
guesses = []
errors = 0

# TODO #1: Set up drawing using Turtle: 
# ------
# |    |
# |
# |
# ------
t = turtle.Turtle()
t.penup()
t.goto(-200,-150)
t.pendown()
t.left(180)
t.forward(90)
t.right(180)
t.forward(180)
t.penup()
t.goto(-200,-150)
t.left(90)
t.pendown()
t.forward(275)
t.right(90)
t.forward(90)
t.right(90)
t.forward(45)
#Start the game loop
choose=int(input("Enter 1 for player-1 or 2 for player-2 mode: "))
if(choose == 2):
  while not game_over:

    guess = input("Guess a letter: ")
    if guess in guesses: 
      print("You already guessed that.")
    else:
      guesses+=guess
    # TODO #2: Check for repeat guess/letter by user and print what letters has been guessed already (hint: using the 'guesses' list)
    
      # TODO #3: Draw next part of hangman using turtle (the stick figure)
      if guess not in word:
        errors += 1
      if errors == 1:
        t.right(90)
        t.circle(30)
      if errors == 2:
        t.right(180)
        t.forward(60)
        t.right(90)
        t.penup()
        t.forward(60)
        t.pendown()
        t.forward(75)
      if errors == 3:
        t.right(35)
      t.forward(60)
      if errors == 4:
        t.right(180)
        t.forward(125)
        t.right(95)
        t.forward(125)
      if errors == 5:
        t.penup()
        t.goto(-110,-10)
        t.left(40)
        t.pendown()
        t.forward(50)
      if errors == 6:
        t.right(180)
        t.forward(200)
      
      #Game losing conditions
      if errors == 6:
        print ("You lose!")
        print ("The word was " + word)
        game_over = True
  
    #Find out if letter is in randomly generated word
    guessed = get_guessed(word, guesses)
    print (guessed)
    
    # Game wining condition
    if guessed == word:
      print ("The word was " + word)
      print ("You win!")
      game_over = True
else:
  print("You have to select player-2 to play the game, Thanks!")
  game_over= True    