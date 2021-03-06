from random import randrange, randint, choice

class bonus():
    
    def __init__(self):
        self.playerTot = 5
        self.computerTot = 5
        self.rounds = 0
        
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
              
class game():
    def __init__(self):
        self.playerScore = 0
        self.computerScore = 0
        self.ties = 0
        self.bestOf = 0
    
    def score(self, playerPoints, computerPoints, tiePoints):
        game.playerScore += playerPoints
        game.computerScore += computerPoints
        game.ties += tiePoints
        if game.playerScore + game.computerScore + game.ties < game.bestOf:
            print "Current score:\nPlayer :", game.playerScore, "Computer: ", game.computerScore
            if game.playerScore == game.computerScore:
                print "Player and computer are tied!"
            elif game.playerScore > game.computerScore:
                print "Player leads!"
            else:
                print "Computer leads!"
            game.next_round()
        else:
            if game.playerScore > game.computerScore:
                print "Player wins the game with a score of ", game.playerScore, "out of ", game.bestOf, "!"
            elif game.playerScore < game.computerScore:
                print "Computer wins the game with a score of ", game.computerScore, "out of ", game.bestOf, "!"
            elif game.playerScore == game.computerScore:
                print "Player and Computer tie the game at ", game.playerScore, "-", game.computerScore
                print "\nIt's time for the bonus round!"
                bonus.bonus_round()
    
    def name_to_number(self, name):
        name = name.lower()
        names = {"rock" : 0, "spock" : 1, "paper" : 2, "lizard" : 3, "scissors" : 4}
        if name in names:
            return names[name]
        else:
            return -1 #entry mispelled or not in game.
            
    def number_to_name(self, number):
        numbers = {0 : "rock", 1 : "Spock", 2 : "paper", 3 : "lizard", 4 : "scissors"}
        return numbers[number]
    
    def next_round(self):
        playerChoice = raw_input("\nInput your choice (rock, Spock, paper, lizard, scissors) : ")
        game.rpsls(playerChoice)
    
    def rpsls(self, name):
        game.bestOf = bestOf
        playerNum = game.name_to_number(name)
        if playerNum >= 0: #check if entry acceptable
            computerNum = randrange(0, 5)
            
            print "Player chooses", name
            print "Computer chooses", game.number_to_name(computerNum)
            
            diff = (playerNum - computerNum) % 5
            
            if diff == 0:
                print "Player and computer tie!\n"
                game.score(0,0,1)
            elif diff <= 2:
                print "Player wins!\n"
                game.score(1,0,0)
            elif diff >= 3:
                print "Computer wins!\n"
                game.score(0,1,0)
        else: #print error if not acceptable
            print "\nERROR : ", name, "is not an accepted entry.\nEntry must be rock, Spock, paper, lizard, or scissors."
         
if __name__ == '__main__' :
        game = game()
        bonus = bonus()
        bestOf = int(raw_input("Input the number of rounds you wish to play: "))
        playerChoice = raw_input("Input your choice (rock, Spock, paper, lizard, scissors) to begin playing : ")
        game.bestOf = bestOf
        game.rpsls(playerChoice)
        #remove next comment if you want to play bonusgame always after rpsls
        #bonus.bonus_round()
 