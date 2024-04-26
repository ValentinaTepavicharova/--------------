import random
import cowsay
from scoreboard import read_scoreboard
from scoreboard import write_scoreboard


print()
print(cowsay.trex("This is Rock/Paper/Scissors Game!"))
print("WELCOME!")
print()
player_name = input("Enter your name here: ")
print()

scoreboard = read_scoreboard()  
user_wins, comp_wins = scoreboard.get(player_name, (0, 0))


answer = ["y", "n"]
options = ("rock", "scissors", "paper")

is_continuous = False

def logic(user_input, comp_pick):
    
    if user_input == "rock" and comp_pick == "scissors":
        print(cowsay.tux("You won!"))
        return "p"
       
    elif user_input == "paper" and comp_pick == "rock":
        print( cowsay.fox("You won!"))
        return "p"
      
    elif user_input == "scissors" and comp_pick == "paper":
        print (cowsay.ghostbusters("You won!") )
        return "p"
     
    elif user_input == comp_pick :
       print("YOU ARE EVEN!") 
       return "e"
  
    else:
        
        print("YOU LOST! :(") 
        return "c"

def points(result):
    global user_wins, comp_wins 
    if result == "p":
        user_wins +=1
        
    if result == "c":
        comp_wins +=1
        
     


while True:
    if is_continuous:
                question = input("Do you want to continue play? Y/N: ").lower()
                print()
                if question == "y":
                    is_continuous = False

                    continue
                elif question == "n":
                    def print_scoreboard(scoreboard):
                        print("\nSCOREBOARD")
                        for name, (user_wins, comp_wins) in scoreboard.items():
                            print(f"{name}: User Wins - {user_wins}, Computer Wins - {comp_wins}")

                    print(f"{player_name} won", user_wins, "times")
                    print("The computer won", comp_wins, "times")
                    print("Goodbye!")
                    scoreboard[player_name] = ( user_wins , comp_wins)
                    write_scoreboard(scoreboard)
                    print_scoreboard(scoreboard)
                    exit()
                if question not in answer:
                    print("Incorrect answer")
                    continue


    user_input = input("Type Rock/Scissors/Paper: ").lower()

    if user_input not in options:
        print("Sorry, I don't understand")
        continue

    random_number = random.choice(range(0, 3))
    comp_pick = options[random_number]
    print("Computer picked", comp_pick + ".")

    winner = logic(user_input, comp_pick)
    points(winner)
    is_continuous = True
   
     