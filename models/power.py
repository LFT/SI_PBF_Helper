import constants
class Power:
    def __init__(self, name, cost, speed, elements, power_type=constants.unique):
        self.name = name
        self.cost = cost
        self.speed = speed
        self.elements = elements
        self.power_type = power_type
        self.target = ""
        
    def __str__(self):
        return "[url=" + constants.query_url+ "\"" + self.name + "\"]" + self.name + "[/url]"