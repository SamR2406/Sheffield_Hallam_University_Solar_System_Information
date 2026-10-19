# Solar System Information

class Planet: # Stores information about each planet
    def __init__(self, name, mass, distance, moons, total_moons):
        self.name = name 
        self.mass = mass  
        self.distance_from_sun = distance 
        self.moons = moons # list of some names of moons
        self.total_moons = total_moons   # Total number of moons
        
    
    def __str__(self):
        if len(self.moons) == 0:
            moon_names = "None"
        else:
            moon_names = ', '.join(self.moons)

        return f"Planet Name: {self.name}\nMass: {self.mass} kg\nDistance from Sun: {self.distance_from_sun} km\nNumber of Moons: {self.total_moons}\nMoons: {moon_names}"


class SolarSystem: # Collects all planets and searches
    def __init__(self):
        self.planets = []  # Store planet objects in a list
        
    def add_planet(self, planet):
        self.planets.append(planet) 
    def find_planet_by_name(self, name):
        for planet in self.planets:
           if planet.name.lower() == name.lower(): # Search through planets without being case sensitive
              return planet
        return None
        
solar_system = SolarSystem()

# List of planets with their atributes from wikipedia
# Distances are measured in kilometers, mass in kilograms and only selected moons are listed.
solar_system.add_planet(Planet("Mercury", 3.3011e23, 57900000, [], 0))
solar_system.add_planet(Planet("Venus", 4.8675e24, 108200000, [], 0))
solar_system.add_planet(Planet("Earth", 5.972e24, 149600000, ["Moon"], 1))
solar_system.add_planet(Planet("Mars", 6.4171e23, 227900000, ["Phobos", "Deimos"], 2))
solar_system.add_planet(Planet("Jupiter", 1.898e27, 778500000, ["Io", "Europa", "Ganymede", "Callisto"], 115))
solar_system.add_planet(Planet("Saturn", 5.683e26, 1434000000, ["Titan", "Rhea", "Iapetus", "Dione", "Tethys", "Enceladus", "Mimas"], 293))
solar_system.add_planet(Planet("Uranus", 8.681e25, 2871000000, ["Miranda", "Ariel", "Umbriel", "Titania", "Oberon"], 29))
solar_system.add_planet(Planet("Neptune", 1.024e26, 4495000000, ["Triton", "Nereid", "Proteus", "Larissa", "Galatea", "Despina", "Thalassa", "Naiad", "Hippocamp"], 16))    

# Sources 
# https://en.wikipedia.org/wiki/Solar_System
# https://en.wikipedia.org/wiki/List_of_natural_satellites

while True: # Main menu 
    print("\n=== Solar System Information ===")
    print("1. Show all planets")
    print("2. Search for a planet")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        for planet in solar_system.planets:
            print(planet.name)

    elif choice == "2":
        name = input("Enter planet name: ").strip()

        while name == "":
            print("Please enter a planet name.")
            name = input("Enter planet name: ").strip()

        planet = solar_system.find_planet_by_name(name)

        if planet is not None: # Shows second menu for the planet the user selects
            while True:
                print(f"\n=== {planet.name} ===")
                print("1. Show all information")
                print("2. Show mass")
                print("3. Show distance from the Sun")
                print("4. Show number of moons")
                print("5. Back to main menu")

                option = input("Enter your choice: ").strip()

                if option == "1":
                    print(planet)

                elif option == "2":
                    print(f"Mass: {planet.mass} kg")

                elif option == "3":
                    print(f"Distance from Sun: {planet.distance_from_sun} km")

                elif option == "4":
                    print(f"Number of moons: {planet.total_moons}")

                elif option == "5":
                    break

                else:
                    print("Invalid choice. Please try again.")

        else:
            print("Planet not found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")


# Sources that helped me with the code:
# https://stackoverflow.com/questions/20252804/str-method-in-python
# https://stackoverflow.com/questions/10443400/how-to-remove-leading-and-trailing-spaces-from-a-string
# https://stackoverflow.com/questions/12453580/how-to-concatenate-join-items-in-a-list-to-a-single-string
# https://stackoverflow.com/questions/25467365/python-menu-driven-programming
