from tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    
    def needs_services(self):
        return sum(self.tire_wear) >= 3.0