from models.player import Player
from starting_data import get_spirit
import random
import constants

class Game:
    def __init__(self, name, fear_stack):
        self.name = name
        self.players = dict()
        self.started = False
        # Todo: init with data
        # Power
        self.available_minor_powers = []
        self.available_major_powers = []        
        self.discard_minor_powers = []
        self.discard_major_power = []
        # Fear
        self.available_fears = []
        self.fear_stack = fear_stack
        self.earned_fears_cards = 0
        self.missing_fear = 0
        self.terror_level = 1
        # Event        
        self.available_events = []
        # Invader
        # Todo later: self.adversary = adversary
        self.next_ravage = []
        self.next_build = []
        self.next_exploration_tier = 1
        # Blight
        self.is_corrupted = False
        self.remaining_blight = 0
    
    def add_player(self, player_name, spirit, color):
        if (not self.started):
            self.players[player_name] = Player(player_name, get_spirit(spirit), color)
            
    def end_growth(self):
        for player_name, player in self.players.items():
            player.end_growth()
            
    def end_turn(self):
        for player_name, player in self.players.items():
            player.end_turn()
            
    def get_x_powers_of_type(self, x, power_type):
        if power_type == constants.major:
            power_array = self.available_major_powers
            power_discard = self.discard_major_powers
        else:
            power_array = self.available_minor_powers
            power_discard = self.discard_minor_powers
        return_powers = power_array[-x:]
        del power_array[-x:]
        if len(return_powers) < x :
            missing_length = x - len(return_powers)
            random.shuffle(power_discard)
            power_array.extend(power_discard)
            power_discard.clear()
            return_powers.extend(self.get_x_powers_of_type(missing_length, power_type))
        return return_powers
    
    def draw_powers_to_disard(self, number_of_power, power_type):
        return_powers = self.get_x_powers_of_type(number_of_power, power_type)
        if power_type == constants.major:
            power_discard = self.discard_major_powers
        else:
            power_discard = self.discard_minor_powers
        power_discard.extend(return_powers)
        return return_powers
    
    def add_to_discard(self, powers_to_discard):
        if powers_to_discard[0].power_type == constants.major:
            power_discard = self.discard_major_powers
        else:
            power_discard = self.discard_minor_powers
        power_discard.extend(powers_to_discard)