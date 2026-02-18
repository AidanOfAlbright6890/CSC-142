# Credit for original code goes to Code Coach on Youtube(Link:https://www.youtube.com/watch?v=mpL0Y01v6tY)

import random
playerIN = True
dealerIn = True
# card deck / player's turn
stack = [2, 3, 4, 5, 6, 7, 8, 9, 10, 
         "J", "Q", "K", "A"]
playersturn = []
dealersturn = []
print("You and the dealer each place down $100.00. Whoever wins gets a fat stash of 200 buckaroos. Good luck fellow gambler.")

# shuffle em up
def dealCard(turn):
    card = random.choice(stack)
    turn.append(card)
    stack.remove(card)

# Calculate the total of each hand
def result(turn):
    result = 0
    face = ["J", "K", "Q"]
    for card in turn:
        if card in range(1, 11):
            result += card
        elif card in face:
            result += 10
        else:
            if result > 11:
                result += 10
            else:
                result += 11
    return result

# And the winner is...
def revealDealersTurn():
    if len(dealersturn) == 2:
        return dealersturn[0]
    elif len(dealersturn) > 2:
        return dealersturn[0], dealersturn[1]

# loop game
for _ in range(1):
    dealCard(dealersturn)
    dealCard(playersturn)

while playerIN or dealerIn:
    print(f" The dealer's got a/an {revealDealersTurn()} and a/an X")
    print(f"On the other hand, you got a/an {playersturn}. Your overall number is {result(playersturn)}")
    print("So what's it gonna be, do you want to get hit, or do you have enough cards?")
    if playerIN:
        stayOrHit = input("1: No more cards please\n2: Hit me(Not literally)\n")
    if result(dealersturn) > 16:
        dealerIn = False
    else:
        dealCard(dealersturn)
    if stayOrHit == '1':
        playerIN = False
    else:
        dealCard(playersturn)
    if result(playersturn) >= 21:
        break
    elif result(dealersturn) >= 21:
        break
if result(playersturn) == 21:
    print(f"\nYou have {playersturn} for a total of {result(playersturn)} and the dealer has {dealersturn} for a total of {result(dealersturn)}")
    print("BLACKJACK! Vicory goes to you! Congratulations fellow gambler.")
elif result(dealersturn) == 21:
    print(f"\nYou have {playersturn} for a total of {result(playersturn)} and the dealer has {dealersturn} for a total of {result(dealersturn)}")
    print("BLACKJACK! Victory goes to the dealer! Sorry, better luck next time fellow gambler.")
elif result(playersturn) > 21:
    print(f"\nYou have {playersturn} for a total of {result(playersturn)} and the dealer has {dealersturn} for a total of {result(dealersturn)}")
    print("Dealer has won the fat stash! Now he's off to buy himself a pet elephant.")
elif result(dealersturn) > 21:
    print(f"\nYou have {playersturn} for a total of {result(playersturn)} and the dealer has {dealersturn} for a total of {result(dealersturn)}")
    print("You have won the fat stash! Now you're off to buy yourself a pet elephant.")
elif 21 - result(dealersturn) > 21 - result(playersturn):
    print(f"\nYou have {playersturn} for a total of {result(playersturn)} and the dealer has {dealersturn} for a total of {result(dealersturn)}")
    print("The dealer beat you!")
elif 21 - result(dealersturn) > 21 - result(playersturn):
    print(f"\nYou have {playersturn} for a total of {result(playersturn)} and the dealer has {dealersturn} for a total of {result(dealersturn)}")
    print("You beat the dealer!")
    
print(dealersturn)
print(playersturn)

