from random import shuffle
def createDeck():
    Deck = []

    faceValues = ["A", "J", "Q", "K"]
    for i in range(4):
        for card in range(2,11):
            Deck.append(str(card))

        for card in faceValues:
            Deck.append(card)
    return Deck

deckValues=createDeck()

shuffle(deckValues)
print(deckValues)

class Player:
    def __init__(self,hand=[],money=100):
        self.hand = hand
        self.score = self.setScore()
        self.money = money
        self.bet = 0

    def __str__(self):
        currentHand = ""

        for card in self.hand:
            currentHand += str(card) + " "
        finalStatus = currentHand + "score: "+ str(self.score)
        return finalStatus

    def setScore(self):
        self.score = 0

        faceCardDict = {"A": 11, "J": 10, "Q": 11, "K": 10, "2": 2, 
                        "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "9": 9,"10": 10}
        aceCounter = 0
        for card in self.hand:
            self.score +=faceCardDict[card]
            if card == "A":
                aceCounter += 1
            if self.score > 21 and aceCounter != 0:
                self.score -= 10
                aceCounter -= 1
        return self.score

    def hit(self,card):
        self.hand.append(card)
        self.score = self.setScore()

    def play(self,newHand):
        self.hand = newHand
        self.score = self.setScore()

    def win(self,result):
        if result == True:
            if self.score == 21 and len(self.hand) == 2:
                self.money += 2.5*self.bet
            else:
                self.money += 2*self.bet

            self.bet = 0
        else:
            self.bet = 0
    def draw(self):
        self.money += self.bet 
        self.bet = 0   

    def betMoney(self, amount):
        self.money -= amount
        self.bet += amount
    def hasBlackjack(self):
        if self.score == 21 and len(self.hand) == 2:
            return True
        else:
            return False

def printHouse(House):
        for card in range(len(House.hand)):
            if card == 0:
                print("X", end=" ")
            elif card== len(House.hand) - 1:
                print(House.hand[card])
            else:
                print(House.hand[card], end = " ")


cardDeck = createDeck()

firstHand = [cardDeck.pop(), cardDeck.pop()]
secondHand = [cardDeck.pop(), cardDeck.pop()]
player1 = Player(firstHand)
House = Player(secondHand)
cardDeck = createDeck()
while (True):
    if len(cardDeck) < 20:
        cardDeck =createDeck()
    firstHand =[cardDeck.pop(), cardDeck.pop()]
    secondHand =[cardDeck.pop(), cardDeck.pop()]
    player1.play(firstHand)
    House.play(secondHand)
    Bet =int(input("Please enter your bet: "))

    print(cardDeck)
    player1.betMoney(Bet)
    print(cardDeck)
    printHouse(House)
    print(player1)

    if player1.hasBlackjack():
        if House.hasBlackjack():
            player1.draw()
        else:
            player1.win(True)
    else:
        while (player1.score < 21):
            action = input("Do you want to input another card? y/n ")
            if action == "y":
                player1.hit(cardDeck.pop())
                print(player1)
                print(House)
            else:
                break
        while (House.score < 16):
            print(House)
            House.hit(cardDeck.pop())
        if player1.score > 21:
            if House.score > 21:
                player1.draw()
            else:
                player1.win(False)
        elif player1.score > House.score:
            player1.win(True)
        elif  player1.score == House.score:
            player1.draw()
        else:
            if House.score > 21:
                player1.win(True)
            else:
                player1.win(False)
    print(player1.money)
    print(House)
# print(cardDeck)
# print(cardDeck.pop())
# print(cardDeck)
# player1 = Player(["3", "7", "6"])

# print(player1)
# player1.hit("K")
# player1.hit("Q")
# print(player1)
# player1.play(["A", "K"])
# print(player1)
# player1.win(True)
# print(player1.money, player1.bet)
# player1.betMoney(50)
# print(player1.money, player1.bet)
