import argparse
import pickle
from models.game import Game
from starting_data import init_game_power

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
        init_game_power(game)
    else :
        with open(filename, "rb") as file:
            game = pickle.load(file)

    if (args.command == "add_player"):
        game.add_player(*args.arguments)
        
    # debugging output
    for player in game.players:
        print(game.players[player].name)
        for power in game.players[player].powers_in_hand:
            print(power.name)
    print(len(game.available_minor_powers),
          len(game.available_major_powers),
          len(game.discard_minor_powers),
          len(game.discard_major_power))
    print(game.available_minor_powers[0].name)
            
    with open(filename, "wb") as file:    
        pickle.dump(game, file)