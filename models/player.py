import constants

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
        self.innate_elements = dict()
        
    def add_energy(self, energy_change):
        self.energy += energy_change
    
    def add_innate(self, element_to_add):
        if element_to_add in self.innate_elements:
            self.innate_elements[element_to_add] += 1
        else:
            self.innate_elements[element_to_add] = 1
    
    def increase_gain(self, gain_increase):
        self.energy_gain += gain_increase
        
    def add_power_choice(self, power_choices):
        self.power_choice.extend(power_choices)
        
    def learn_power(self, name):
        found_power = find_and_remove_power(search_string, self.power_choice)
        if found_power:
            self.powers_in_hand.append(found_power)
            power_to_discard = self.power_choice.copy()
            self.power_choice = []
            return power_to_discard
            
    def end_growth(self):
        self.add_energy(self.energy_gain)
        
    def end_turn(self):
        self.powers_in_discard.extend(self.slow_powers_played)
        self.powers_in_discard.extend(self.fast_powers_played)
        self.slow_powers_played = []
        self.fast_powers_played = []
        
    def reclaim_all(self):
        self.powers_in_hand.extend(self.powers_in_discard)
        self.powers_in_discard = []
    
    def reclaim_one(self, search_string):
        found_power = find_and_remove_power(search_string, self.powers_in_discard)
        if found_power:
            self.powers_in_hand.append(found_power)
            
    def play_power(self, search_string):
        found_power = find_and_remove_power(search_string, self.powers_in_hand)
        if found_power:
            self.energy -= found_power.cost
            if found_power.speed == constants.slow:
                self.slow_powers_played.append(found_power)
            else:
                self.fast_powers_played.append(found_power)
    
    def forget_power(self, search_string):
        found_power = find_and_remove_power(search_string, self.powers_in_hand)
        if not found_power:
            found_power = find_and_remove_power(search_string, self.slow_powers_played)
        if not found_power:
            found_power = find_and_remove_power(search_string, self.fast_powers_played)
        if not found_power:
            found_power = find_and_remove_power(search_string, self.powers_in_discard)
        return found_power
    
    def accelerate_power(self, search_string):
        found_power = find_and_remove_power(search_string, self.slow_powers_played)
        if found_power:
            self.fast_powers_played.append(found_power)
        
    def find_and_remove_power(search_string, power_list):
        found_power = None
        for power in power_list:
            if search_string in power.name:
                found_power = power
        if found_power:
            power_list.remove(found_power)
        return found_power