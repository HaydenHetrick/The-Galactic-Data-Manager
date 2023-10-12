# Lab: The Galactice Data Manager
# defining starship classes
class Starship:
    def __init__(self, name, model, role, crew_size):
        self.name = name
        self.model = model
        self.role = role
        self.crew_size = crew_size
# returns formatted string of starships details
def get_info(self):
    return f"Starship: {self.name}\nModel: {self.model}\nRole: {self.role}|nCrew Size: {self.crew_size}\n"

# converts starship data to a dictionary and returns it 
def to_dict(self):
    return {
        "name": self.name,
        "model": self.model,
        "role": self.role,
        "crew_size": self.crew_size,
    }

# defining GalacticDataManager class
class GalacticDataManager:
    def __init__(self):
        self.data = {}

# adds a starship object to data
def add_starship(self, starship):
    self.data[starship.name] = starship.to_dict()

# prints all stored starship data
def display_all_starships(self):
    for starship_name, starship_data in self.data.items():
        print(f"{starship_name}:")
    for attribute, value in starship_data.items():
        print(f"    {attribute.capitalize()}: {value}")
    print("\n")

# Creating instances of starships
death_star = Starship("The Death Star", "Orbital Battle Station", "Plant Killer", 1206293)
super_star_destroyer = Starship("Super Star Destroyer", "Sovereign Class", "Super Destroyer", 280000)
star_destroyer = Starship("Star Destroyer", "Imperial I-class", "Destroyer", 37000)
supremacy = Starship("Supremacy", "Mega Class Star Dreadnought", "Dreadnought", 2225000)
tie_fighter = Starship("Tie Fighter", "Space Superiority Fighter", "Fighter", 1)
borg_cube = Starship("Borg Cube", "7,189 B", "Interstellar Transport & Combat Vessel", 179000)
unsc_pillar_of_autumn = Starship("UNSC Pillar Of Autumn", "Halcyon Class", "Durability", 1200)

# instantiating the GalacticDataManager and adding the starships to it 
galactic_data_manager = GalacticDataManager()
galactic_data_manager.add_starship(death_star)
galactic_data_manager.add_starship(super_star_destroyer)
galactic_data_manager.add_starship(star_destroyer)
galactic_data_manager.add_starship(supremacy)
galactic_data_manager.add_starship(tie_fighter)
galactic_data_manager.add_starship(borg_cube)
galactic_data_manager.add_starship(unsc_pillar_of_autumn)

# displaying all starships and there info
galactic_data_manager.display_all_starships()


