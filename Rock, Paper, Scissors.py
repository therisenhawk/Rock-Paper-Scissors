import random

valid_moves = ("rock", "paper", "scissors") #stored in a tuple. cant be changed

def get_user_move():

    #function asks user to make their choice

    while True:

        user_choice = input("Choose rock, paper, scissors or quit: ").lower()
        if user_choice == "quit":
            return "quit"
        if user_choice in valid_moves:
            return user_choice
        else:
            print("Please choose rock, paper, scissors or quit. ")
            
def get_computer_move():

    #function that returns computer's random move
    pick_move = random.choice(valid_moves)
    return pick_move

def determine_the_winner(player_move, computer_move):

    #function compares player's choice to computer's choice and sorts who won or if it's a tie

    if player_move == computer_move:
        return "tie"
    elif player_move == "rock" and computer_move == "scissors":
        return "win"
    elif player_move == "scissors" and computer_move == "paper":
        return "win"
    elif player_move == "paper" and computer_move == "rock":
        return "win"
    else:
        return "lose"

def play_endless_mode():

     #function allows the player to play indefinitely
    win = 0
    lose = 0
    tie = 0
    
    
    while True:

        player_move = get_user_move()   #stores the return from the get_user_move function. Basically it will be rock, paper, scissors or quit
        if player_move == "quit":
            print("You quit the game")
            print(f"Final score: Wins: {win}, Loses: {lose}, Draw: {tie}")
            break

        computer_move = get_computer_move() #stores the return from get_computer_move() which is rock, paper or scissors
        print(f"Computer chose: {computer_move}")

        result = determine_the_winner(player_move, computer_move) #stores return from determine_the_player(); which is win/lose/draw
        if result == "win":
            win += 1
            print("You won this round!")
        elif result == "lose":
            lose += 1
            print("You lost this round :(.") 
        else:
            tie += 1
            print("It's a tie!")  

        print(f"Score → Wins: {win}, Losses: {lose}, Ties: {tie}")        
        print("-" * 70)

def play_match(best_of):

    #function lets the player choose to play best of 3 or 5 games

    wins_needed = best_of // 2 + 1    
    players_wins = 0
    computers_wins = 0

    while players_wins < wins_needed and computers_wins < wins_needed:

        players_move = get_user_move()  #stores player's move
        if players_move == "quit":
            print("You quit the match early.")  #making a difference between losing and quitting the match
            return
        computers_move = get_computer_move()    #stores computer's move
        print(f"Computer chose: {computers_move}")
        result = determine_the_winner(players_move, computers_move) #stores win, lose or tie based on the player's and computer's choice
        if result == "win":
            players_wins += 1
        elif result == "lose":
            computers_wins += 1
        elif result == "tie":
            print("It's a tie")
            continue    
        print(f"Player's score: {players_wins}, Computer's score: {computers_wins}")

    if players_wins > computers_wins:
        print("You won the match!")
    else:
        print("You lost the match.")

def main():

    # creates a menu to choose from game modes and calls previous functions
    while True:
        print("Menu:\n 1 - endless mode\n 2 - best of 3\n 3 - best of 5\n q - quit ")

        choice = input("Choose the game mode: ").lower()

        if choice == "q":
            print("Thanks for playing. Goodbye")
            break

        if choice == "1":
            play_endless_mode()
        elif choice == "2":
            play_match(3)
        elif choice == "3":
            play_match(5)   
        else:
            print("Invalid input. Try again")        




if __name__ == "__main__":
    main()