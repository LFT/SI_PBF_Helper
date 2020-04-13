from models.player import Player
from starting_data import get_spirit
class Game:
    def __init__(self, name, fear_stack):
        self.name = name
        self.players = []
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
            self.players.append(Player(player_name, get_spirit(spirit), color))