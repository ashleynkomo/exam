import pickle

class Game:
    def __init__(self):
        self.Name = None
        self.Platform = None
        self.Genre = None
        self.Cost = None
        self.Players = None
        self.Online_functionality = None

def load_games(filename):
    with open(filename, mode = "rb") as Games_Record:
        games = pickle.load(Games_Record)
    return games

def save_games(filename, games):
    with open(filename, mode="wb") as filename:
        pickle.dump(games,filename)


def display_games(games):
    print("|{0:<15}|{1:<15}|{2:<15}|{3:<15}|{4:<15}|{5:<15}|".format("Name", "Platform", "Genre", "Cost", "Players", "Online functionality"))
    print("------------------------------------------------------------------------------------------------------")
    
    for game in games:
        print("|{0:<15}|{1:<15}|{2:<15}|{3:<15}|{4:<15}|{5:<15}|".format(game.Name, game.Platform, game.Genre, game.Cost, game.Players, game.Online_functionality))
    

def get_game_from_user(games):
    done = False
    while not done:
        Name = input("Please enter the name of the game: ")
        if Name == "-1":
            print("You have closed the program")
            done = True
        else:
            game = Game()
            game.Name = Name
            game.Platform = input("Please enter the platform of the game: ")
            game.Genre = input("Please enter the genre of the game: ")
            game.Cost = float(input("Please enter the price of the game: "))
            game.Players = int(input("Please enter the number of players: "))
            game.Online_functionality = input("Is the game online or not: ")
            games.append(game)
            
    return games

def display_menu():
    print()
    print("***Welcome to the Computer and Video Game Database***")
    print()
    print("1. Add new games")
    print("2. Display games")
    print("3. Exit program")
    print()

def main():
    exit_program = False
    try:
        
        filename = input("What's the filename:")
        games = load_games(filename)
    except FileNotFoundError:
        print("No file to load")
        games = []
    while not exit_program:
        display_menu()
        try:
            selected_option = int(input("Please select a menu option: "))
            if selected_option == 1:
                games = get_game_from_user(games)
            elif selected_option == 2:
                display_games(games)
            elif selected_option == 3:
                save_games(filename,games)
                exit_program = True
            else:
                print("Please enter a valid option (1-3)")
        except ValueError:
            print("Please enter a valid option (1-3)")
            print("")

if __name__ == "__main__":
    main()
