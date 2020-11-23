import random
money = 100

#High/Low Card Game
hi = "high"
lo = "low"

def high_low(bet, hi_or_lo, number_of_games):
    global money
    card_number = list(range(1,14))*4
    card_type = ['diamonds', 'clubs', 'hearts', 'spades']*13
    for game in range(number_of_games):
        while money >= bet and game < number_of_games:
            card_deck = list(zip(card_number, card_type))
            player_draw = []
            player_draw.append(random.choice(card_deck))
            card_deck.remove(player_draw[0])
            house_draw = [random.choice(card_deck)]
            if (player_draw[0] > house_draw[0] and hi_or_lo == hi) or (player_draw[0] < house_draw[0] and hi_or_lo == lo):
                money += bet
                print("Winner is {}, Congratulations! You won ${}, drawing a {} of {} against the House draw, {} of {}. You're new total is ${}.".format(hi_or_lo, bet, *player_draw[0], *house_draw[0], money))
                game += 1
            elif (player_draw[0] < house_draw[0] and hi_or_lo == hi) or (player_draw[0] > house_draw[0] and hi_or_lo == lo):
                money -= bet
                print("The result is not {}, I'm sorry. You lost ${}, drawing a {} of {} against the House draw, {} of {}. You're new total is ${}.".format(hi_or_lo, bet, *player_draw[0], *house_draw[0], money))
                game += 1
            elif player_draw[0] == house_draw[0]:
                print("The result is a tie, with your draw, {} of {}, and the house draw, {} of {}. Your total is unchanged, at ${}.".format( *player_draw[0], *house_draw[0], money))
                game += 1
        if game == number_of_games:
            return "Thanks for playing!"
        else:    
            return "You do not have enough money to cover your bet. Thanks for playing!"

#Call your game of chance functions here

print(high_low(50, hi, 5))


Reply
Suggested Topics