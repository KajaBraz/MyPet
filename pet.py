from attributes_coeficients import min_level, max_level


class PetAttributes:
    def __init__(self, bond=50, food=500, energy=500, hygiene=500, happiness=50, poo=500):
        self.bond = bond
        self.food = food
        self.energy = energy
        self.hygiene = hygiene
        self.happiness = happiness
        self.poo = poo

    def __repr__(self):
        return f"bond: {self.bond} \nfood: {self.food} \nenergy: {self.energy} \nhygiene: {self.hygiene} \nhappiness: {self.happiness} \npoo: {self.poo} "

    def is_fine(self):
        if self.bond < min_level or self.food < min_level or self.energy < min_level or self.hygiene < min_level or self.happiness < min_level or self.poo > max_level:
            return False
        return True
