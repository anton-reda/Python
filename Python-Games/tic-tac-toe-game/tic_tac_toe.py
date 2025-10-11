import os

def clear_screen():
    os.system("cls")

class Player :
    def __init__(self):
        self.name = ""
        self.symbol = ''

    def choose_name(self):
        while True:
            name = input("Enter you name : ")
            if name.isalpha():
                self.name = name 
                break
            print("Invalid name. please use letters only")
        
            

    def choose_symbol(self):
         while True:
            symbol = input(f"{self.name} Choose your symbol : ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid symbol. please choose a single character ")


class Menu:
    def display_main_menu(self):
        print("welcome to my X-O game!")
        print("1. Start game ")
        print("2. End game")
        while True:
            choice = input("Enter your choice (1 or 2 ) : ")
            if choice.isdigit() and choice in {"1", "2"}:
                return int(choice) 
            print("Invalid input , please enter 1 or 2 ")
    
    
       
    
    def display_endgame_menu(self):
        print(" Game Over !") 
        print("1. Restart Game") 
        print("2. Quit game ") 
        while True:
            choice = input("Enter your choice (1 or 2 ) :")
            if choice.isdigit() and choice in {"1", "2"}:
                return int(choice) 
            print("Invalid input , please enter 1 or 2 ") 


class Board :
    def __init__(self):
        self.board = [str(i) for i in range(1,10)]

    def display_board(self):
        for i in range (0,9,3):
            print(" | ".join(self.board[i:i+3]))
            if i < 6 :
                print("-" * 9)

    def valid_choice(self,choice):
       # return self.board[choice - 1] in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        return self.board[choice - 1].isdigit()

    def update_board (self,symbol,choice):
        if self.valid_choice(choice):
            self.board[choice - 1] = symbol
            return True
        return False
    
    def reset_board(self):
        self.board = [str(i) for i in range(1,10)]

class Game:
    def __init__(self):
        self.players = [ Player() , Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0 
    
    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == 1:
            self.setup_game()
            self.play_game()
        else:
            self.quit_game()

    # def setup_game(self):
    #     number = 1
    #     for player in self.players:
    #         print( "-" *30, "\n" , f"Player {number} " )
    #         number += 1
    #         player.choose_name()        
    #         player.choose_symbol()
    #         clear_screen()
    def setup_game(self):
        for number,player in enumerate(self.players, start= 1):
            print( "-" *30, "\n" , f"Player {number} " )
            player.choose_name()        
            player.choose_symbol()
            clear_screen()
        

    def play_game(self):
        while True:
            self.play_turn()
            player = self.players[self.current_player_index - 1 ]
            if self.check_win() or self.check_draw():
                if self.check_win():
                    self.board.display_board()
                    print("\n", f"{player.name} Wins!")
                if self.check_draw():
                    self.board.display_board()
                    print("\n","Draw !")
                choice = self.menu.display_endgame_menu()
                if choice == 1:
                    self.restart_game()
                else:
                    self.quit_game()
                    break

                 
    
    def restart_game(self):
       self.board.reset_board()
       self.current_player_index = 0 
       clear_screen()
       self.play_game()
        
    def check_win(self):
        win_combinations = [
            [0,1,2] , [3,4,5] , [6,7,8], # rows
            [0,3,6] , [1,4,7] , [2,5,8], # columns
            [0,4,8] , [2,4,6]]           # diagonals
        
        for combo in win_combinations:
            if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]:
                return True
        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def play_turn(self): 
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")  
        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9) : "))
                if 1<= cell_choice <= 9 and self.board.update_board(player.symbol , cell_choice):
                    clear_screen()
                    break
                print("Invalid move , try agian.")
            except ValueError:
                print("please enter a number between 1 and 9 ")
        self.switch_player()
    
    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index 


    def quit_game(self):
        print("Thank you for playing")

game = Game()
game.start_game()