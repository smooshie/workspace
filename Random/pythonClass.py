from random import randrange, randint, choice


class bonus():
    
    def __init__(self):
        self.playerTot = 5
        self.computerTot = 5
        
    def heads_or_tails(self):
        sides = ["heads", "tails"]
        print "Double Round: Heads or Tails!\n"
        playerSide = raw_input("Choose heads or tails : ").lower().lstrip().rstrip()
        print "Player chooses ", playerSide
        winner = choice(sides)
        if playerSide == winner:
            print "Tossed coin: ", winner
            print "Player wins, winnings doubled!"
            print "Player earns 10 coins."
            return 1
        else:
            print "Tossed coin: ", winner
            print "Player loses, gains no winnings."
            return 0
    
    def correct(self):
        print "Player wins!\n"
        hot = raw_input("Do you want to try to double? (y/n)" )
        if hot == "y":
            double = bonus.heads_or_tails()
            if double == 1:
                bonus.playerTot += 10
        else:
            bonus.playerTot += 5
            
    def currentPoints(self):
        print "Player's current points: ", bonus.playerTot
        print "Computer's current points: ", bonus.computerTot
        
    def bonus_round(self):
        print "Bonus Round: High or Low!\n"
        print "Both players start the game with 5 coins. Every round of the game costs one coin. You will be presented with a card, you must choose whether you think the next drawn card is higher or lower."
        print "If you choose correctly you win 5 coins. You can then choose to try to double your winnings in a game of heads or tails. If you choose right you win 5 extra coins, if you choose wrong you lose your winnings."
        print "The game ends when one either runs out of coins or has a total of 20 coins."
        choices = ["higher", "lower"]
        cards = {1 : "Ace", 2: "Two", 3 : "Three", 4 : "Four", 5 : "Five", 6 : "Six", 7 : "Seven", 8 : "Eight", 9 : "Nine", 10 : "Ten", 11 : "Jack", 12 : "Queen", 13 : "King"}
        while (self.playerTot != 0 or self.computerTot != 0) and (self.playerTot < 20 or self.computerTot < 20):
            card = randint(1, 13)
            nextCard = randint(1, 13)
            if card == nextCard :
                nextCard = randint(1, 13)
            print "\nCard is :", cards[card]
            playersChoice = raw_input("Is the next card higher or lower : ").lower().lstrip().rstrip()
            bonus.playerTot = bonus.playerTot - 1
            print "Next card is : ", cards[nextCard]
            if  (playersChoice == "higher" and nextCard > card) or (playersChoice == "lower" and nextCard < card):
                bonus.correct()
            elif playersChoice == "higher" and nextCard < card:
                print "Player chose higher when next card was lower, no winnings."
            elif playersChoice == "lower" and nextCard > card:
                print "Player chose lower when next card was higher, no winnings."
            bonus.currentPoints()
            
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
        try:
            return names[name]
        except KeyError:
            print "\nERROR : ", name, "is not an accepted entry.\nEntry must be rock, spock, paper, lizard, or scissors."
            exit(0)
            
    def number_to_name(self, number):
        numbers = {0 : "rock", 1 : "Spock", 2 : "paper", 3 : "lizard", 4 : "scissors"}
        return numbers[number]
    
    def next_round(self):
        playerChoice = raw_input("\nInput your choice (rock, Spock, paper, lizard, scissors) : ")
        game.rpsls(playerChoice)
    
    def rpsls(self, name):
        game.bestOf = bestOf
        playerNum = game.name_to_number(name)
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
                
if __name__ == '__main__' :
        game = game()
        bonus = bonus()
        bestOf = int(raw_input("Input the number of rounds you wish to play: "))
        playerChoice = raw_input("Input your choice (rock, Spock, paper, lizard, scissors) to begin playing : ")
        game.bestOf = bestOf
        game.rpsls(playerChoice)
 