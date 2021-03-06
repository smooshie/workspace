'''
Created on 24.4.2013

@author: lisagawr
'''
from random import randrange, randint, choice

class bonus():
    
    def __init__(self):
        self.playerTot = 5
        self.computerTot = 5
        self.rounds = 0
        self.fullLoop = False
        
    def heads_or_tails(self):
        sides = ["heads", "tails"]
        print "Double Round: Heads or Tails!\n"
        playerSide = raw_input("Choose heads or tails : ").lower().lstrip().rstrip()
        while playerSide not in sides:
            playerSide = raw_input("Wrong input. Choose heads or tails : ").lower().lstrip().rstrip()
        print "Player chooses ", playerSide
        winner = choice(sides)
        print "Tossed coin: ", winner
        if playerSide == winner:
            print "Player wins, winnings doubled!"
            print "Player earns 10 coins.\n"
            bonus.playerTot += 10
        else:
            print "Player loses, gains no winnings.\n"
    
    def correct(self, who):
        if who == "Player":
            hot = raw_input("Do you want to try to double? (y/n) ")
            while hot != "y" and hot != "n":
                hot = raw_input("Wrong input. Do you want to try to double? Write y for yes, n for no.")
            if hot == "y":
                double = bonus.heads_or_tails()
            elif hot == "n":
                print "Player chose not to double."
                bonus.playerTot += 5
              
        if who == "Computer":
            hot = randint(0,1)
            cdouble = randint(0,1)
            if hot == 1:
                if cdouble == 1:
                        print "Computer guessed the tossed coin right and gains 10 coins!"
                        bonus.computerTot += 10
            else:
                print "Computer chose not to double."
                bonus.computerTot += 5
              
    def correct_or_not(self, who, choice, card, nextCard):
        if choice == "higher" and nextCard < card:
            print who, "chose higher when next card was lower, no winnings."
        elif choice == "lower" and nextCard > card:
            print who, "chose lower when next card was higher, no winnings."
        elif  (choice == "higher" and nextCard > card) or (choice == "lower" and nextCard < card):
            print who, "chose right!"
            bonus.correct(who)
               
    def currentPoints(self):
        print "\nPlayer's current points: ", bonus.playerTot
        print "Computer's current points: ", bonus.computerTot
        
    def bonus_round(self):
        print "Bonus Round: High or Low!\n"
        print "Both players start the game with 5 coins. Every round of the game costs one coin. You will be presented with a card, you must choose whether you think the next drawn card is higher or lower."
        print "If you choose correctly you win 5 coins. You can then choose to try to double your winnings in a game of heads or tails. If you choose right you win 5 extra coins, if you choose wrong you lose your winnings."
        print "The game ends when one either runs out of coins or has a total of 20 coins."
        choices = ["higher", "lower"]
        cards = {1 : "Ace", 2: "Two", 3 : "Three", 4 : "Four", 5 : "Five", 6 : "Six", 7 : "Seven", 8 : "Eight", 9 : "Nine", 10 : "Ten", 11 : "Jack", 12 : "Queen", 13 : "King"}
        while self.playerTot != 0 and self.computerTot != 0 and self.playerTot < 20 and self.computerTot < 20:
            self.rounds += 1
            card = randint(1, 13)
            nextCard = randint(1, 13)
            while card == nextCard :
                nextCard = randint(1, 13)
            if bonus.playerTot - 1 > 0 or bonus.computerTot - 1 > 0:
                bonus.playerTot = bonus.playerTot - 1
                bonus.computerTot = bonus.computerTot - 1
            else:
                break
            print "\nCard is :", cards[card]
            playersChoice = raw_input("Is the next card higher or lower : ").lower().lstrip().rstrip()
            while playersChoice not in choices:
                print "Wrong entry! You entered : ", playersChoice
                playersChoice = raw_input("Please enter 'higher' or 'lower' : ")
            if card <= 4:
                computersChoice = "higher"
            elif card >= 8:
                computersChoice = "lower"
            else:
                computersChoice = choice(choices)
            print "Computer chooses :", computersChoice
            print "Next card is : ", cards[nextCard]
            bonus.correct_or_not("Player", playersChoice, card, nextCard)
            bonus.correct_or_not("Computer", computersChoice, card, nextCard)
            bonus.currentPoints()
            
        if self.playerTot <= 0:
            print "Player coins reached 0, player lost."
        elif self.playerTot >= 20 and self.computerTot < 20:
            print "Player coins reached 20, player won!"
            print "\nCongratulations player!"
        elif self.computerTot <= 0:
            print "Computer coins reached 0, player won!"
        elif self.computerTot >= 20 and self.playerTot < 20:
            print "Computer coins reached 20, computer won!"
        elif self.computerTot >= 20 and self.playerTot >= 20:
            print "Both players reached 20 on the same turn! How is this possible?! Go play some other game!"
            
if __name__ == '__main__' :
        bonus = bonus()
        bonus.bonus_round()