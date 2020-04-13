import argparse
import pickle
from models.game import Game

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="The name of the game that's to be modified")
    parser.add_argument("command", help="The command you want to run")
    args = parser.parse_args()
    filename = args.name + ".data"
    if (args.command != "init"):
        with open(filename, "rb") as file:
            game = pickle.load(file)
    else :
        game = Game(args.name,"3/3/3")
    print(game.name)
    with open(filename, "wb") as file:    
        pickle.dump(game, file)