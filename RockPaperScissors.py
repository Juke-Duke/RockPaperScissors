import random

class WinRate:
  win = 0
  loss = 0
  tie = 0

#function for inputing your option
def RockPaperScissors_Choice():
  options = ['Rock','Paper','Scissors']
  choice = input("Type Rock,Paper,Scissors [STATS/QUIT]: ")
  while choice.lower() not in ['rock','paper','scissors','quit','stats']:
    print("Illegal Command Buddy Boi")
    choice = input("Type Rock,Paper,Scissors: ")
  if choice.lower() == 'quit':
    quitGame(choice)
  elif choice.lower() == 'stats':
    Winrate()
  else:
    print("---Match---")
   #CPU choice
    CPUChoice = random.choice(options)
    print("CPU chooses " + CPUChoice)
    #determine winner
    RockPaperScissors_Results(choice,CPUChoice)

#function for showing results of the choice you inputed in the RockPaperScissors_Choice function
def RockPaperScissors_Results(choice,CPUChoice):
  #shows each result of every possible option
  if choice.lower() == CPUChoice.lower():
    print("TIE\n")
    tieADD()
  elif choice.lower() == "rock" and CPUChoice.lower() == "paper":
    print("Paper covers Rock, CPU WINS\n")
    lossADD()
  elif choice.lower() == "rock" and CPUChoice.lower() == "scissors":
    print("Rock crushes Scissors, YOU WIN\n")
    winADD()
  elif choice.lower() == "paper" and CPUChoice.lower() == "rock":
    print("Paper covers Rock, YOU WIN\n")
    winADD()
  elif choice.lower() == "paper" and CPUChoice.lower() == "scissors":
    print("Scissors cuts Paper, CPU WINS\n")
    lossADD()
  elif choice.lower() == "scissors" and CPUChoice.lower() == "rock":
    print("Rock crushes Scissors, CPU WIN\n")
    rate.loss += 1
  elif choice.lower() == "scissors" and CPUChoice.lower() == "paper":
    print("Scissor cuts Paper, YOU WIN\n")
    winADD()
  RockPaperScissors_Choice()

#shows stats when user types STATS and then runs the game again
def Winrate():
  print("---Stats---")
  print("Wins:",rate.win, "\nLosses:",rate.loss, "\nTies:",rate.tie, "\n")
  RockPaperScissors_Choice()

#quits game when user types QUIT
def quitGame(command):
  if command.lower() == "quit":
    print("Good Game")
  
#changes stats based off result of RockPaperScissors_Results
def winADD():
  rate.win += 1
def lossADD():
  rate.loss += 1
def tieADD():
  rate.tie += 1

def main():
  print("Type 'Quit' anytime to quit and 'Stats' for seeing total stats\n")
  global rate
  rate = WinRate()
  RockPaperScissors_Choice()
if __name__ == "__main__":
  main()
