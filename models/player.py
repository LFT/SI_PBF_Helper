class Player:
    # The player will have all the varying stuff
    # Its stock of energy, energy gain, cards in hand/discard and such.
    def __init__(self, name, spirit, color):
        self.name = name
        self.spirit = spirit
        self.color = color
        self.energy = 0
        self.energy_gain = spirit.base_energy_gain
        self.powers_in_hand = spirit.powers.copy()
        self.power_choice = []
        self.slow_powers_played = []
        self.fast_powers_played = []
        self.powers_in_discard = []
        self.innate_elements = []