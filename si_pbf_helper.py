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

    # command used during setup
    if (args.command == "add_player"):
        game.add_player(*args.arguments)
    # commands used during the flow of the game
    elif (args.command == "end_growth"):
        for player_name, player in game.players.items():
            player.end_growth()
    elif (args.command == "end_turn"):
        for player_name, player in game.players.items():
            player.end_turn()
    # all the command below are used specifically for one player
    else:
        player_name = args.arguments[0]
        del args.arguments[0]
        if not player_name in game.players:
            raise ValueError("Incorrect player name")
        player = game.players[player_name]
        # energy
        if (args.command == "gain"):
            player.increase_gain(*args.arguments)
        elif (args.command == "energy"):
            player.add_energy(*args.arguments)
        # powers
        #add_power_choice
        #learn_power
        #reclaim_all
        #reclaim_one
        #play_power
        #forget_power
        #accelerate_power
        # elements
        elif (args.command == "element"):
            player.add_innate_element(*args.arguments)
    # debugging output
    for player_name, player in game.players.items():
        print(player.name, player.energy)
        for power in player.powers_in_hand:
            print(power.name)
    print(len(game.available_minor_powers),
          len(game.available_major_powers),
          len(game.discard_minor_powers),
          len(game.discard_major_power))
    print(game.available_minor_powers[0].name)
            
    with open(filename, "wb") as file:    
        pickle.dump(game, file)