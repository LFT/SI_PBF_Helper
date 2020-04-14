import argparse
import pickle
from models.game import Game
from starting_data import init_game_power

if __name__ == '__main__':
    def get_check_player(player_name):
        if not player_name in game.players:
            raise ValueError("Incorrect player name")
        return game.players[player_name]
    
    # Commands used during game setup
    def add_player(args):
        game.add_player(args.player_name, args.spirit, args.color)
    
    # Commands used during the flow of the game    
    def end_growth(args):
        game.end_growth()
            
    def end_turn(args):
        game.end_turn()
        
    # Commands used specifically for one player
    # Energy
    def increase_gain(args):
        player = get_check_player(args.player_name)
        player.increase_gain(args.energy)
    
    def add_energy(args):
        player = get_check_player(args.player_name)
        player.add_energy(args.energy)
        
    # powers
        #add_power_choice
        #learn_power
        #reclaim_all
        #reclaim_one
        #play_power
        #forget_power
        #accelerate_power
        
    # elements
    def add_innate_element(args):
        player = get_check_player(args.player_name)
        player.add_innate_element(args.element_name)
        
        
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="The name of the game that's to be modified")
    subparsers = parser.add_subparsers(dest="command")
    parser_init = subparsers.add_parser('init', help="Initialize the game")
    parser_growth = subparsers.add_parser('growth', help="End growth")
    parser_growth.set_defaults(func=end_growth)
    parser_turn = subparsers.add_parser('turn', help="End turn")
    parser_turn.set_defaults(func=end_turn)
    parser_add_player = subparsers.add_parser('player', help="Add a player to the game")    
    parser_add_player.add_argument('player_name')
    parser_add_player.add_argument('spirit')
    parser_add_player.add_argument('color')
    parser_add_player.set_defaults(func=add_player)
    parser_increase_gain = subparsers.add_parser('gain', help="Change a player energy gain per turn")    
    parser_increase_gain.add_argument('player_name')
    parser_increase_gain.add_argument('energy', type=int)
    parser_increase_gain.set_defaults(func=increase_gain)
    parser_add_energy = subparsers.add_parser('energy', help="Change a player energy count")    
    parser_add_energy.add_argument('player_name')
    parser_add_energy.add_argument('energy', type=int)
    parser_add_energy.set_defaults(func=add_energy)
    parser_add_innate_element = subparsers.add_parser('element', help="Add one innate element to a player")    
    parser_add_innate_element.add_argument('player_name')
    parser_add_innate_element.add_argument('element_name')
    parser_add_innate_element.set_defaults(func=add_innate_element)
    parser_power_choice = subparsers.add_parser('choice', help="Add X powers to chose from to a player")    
    parser_power_choice.add_argument('player_name')
    parser_power_choice.add_argument('number_of_power')
    parser_power_choice.add_argument('type_of_power', type=int)
    #parser_power_choice.set_defaults(func=power_choice)
    parser_learn_power = subparsers.add_parser('learn', help="Add a power to the player's hand")    
    parser_learn_power.add_argument('player_name')
    parser_learn_power.add_argument('power_string')
    #parser_learn_power.set_defaults(func=learn_power)
    parser_reclaim_all = subparsers.add_parser('reclaim_all', help="Reclaim all of a player's powers")    
    parser_reclaim_all.add_argument('player_name')
    #parser_reclaim_all.set_defaults(func=reclaim_all)
    parser_reclaim_one = subparsers.add_parser('reclaim_one', help="Reclaime one of a player's power")    
    parser_reclaim_one.add_argument('player_name')
    parser_reclaim_one.add_argument('power_string')
    #parser_reclaim_one.set_defaults(func=reclaim_one)
    parser_forget_power = subparsers.add_parser('forget', help="Forget one of a player's power")    
    parser_forget_power.add_argument('player_name')
    parser_forget_power.add_argument('power_string')
    #parser_forget_power.set_defaults(func=forget_power)
    parser_accelerate_power = subparsers.add_parser('accelerate', help="Accelerate one of a player's power")    
    parser_accelerate_power.add_argument('player_name')
    parser_accelerate_power.add_argument('power_string')
    #parser_accelerate_power.set_defaults(func=accelerate_power)
    parser_play_power = subparsers.add_parser('play', help="Play one of a player's power")    
    parser_play_power.add_argument('player_name')
    parser_play_power.add_argument('power_string')
    #parser_play_power.set_defaults(func=play_power)

    args = parser.parse_args()
    filename = args.name + ".data"
    # initialising the Game object. Either a new one or loading the existing one.
    if (args.command == "init"):
        game = Game(args.name,"3/3/3")
        init_game_power(game)
    else :
        with open(filename, "rb") as file:
            game = pickle.load(file)
        args.func(args)
    
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
        