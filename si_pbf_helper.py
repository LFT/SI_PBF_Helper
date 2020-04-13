import argparse
import pickle
from models.game import Game

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="The name of the game that's to be modified")
    parser.add_argument("command", help="The command you want to run")
    parser.add_argument("arguments", help="arguments for your command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    filename = args.name + ".data"
    # initialising the Game object. Either a new one or loading the existing one.
    if (args.command == "init"):
        game = Game(args.name,"3/3/3")
    else :
        with open(filename, "rb") as file:
            game = pickle.load(file)

    if (args.command == "add_player"):
        game.add_player(*args.arguments)
        
    with open(filename, "wb") as file:    
        pickle.dump(game, file)