class Game:
    def __init__(self, name, fear_stack):
        self.name = name
        self.players = []
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
        self.is_corrupted = false
        self.remaining_blight = 0