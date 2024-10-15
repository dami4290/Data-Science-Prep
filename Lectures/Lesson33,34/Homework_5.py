import random

class Move:
    def __init__(self, name, p_type, damage):
        """
        Initialize a Move object representing a Pokémon move (attack).

        Args:
            name (str): The name of the move.
            p_type (str): The type of the move (e.g., 'Water', 'Fire').
            damage (int): The base damage of the move.
        """
        self.name=name
        self.p_type=p_type
        self.damage=damage
    

        self.not_effective=[]
        self.very_effective=[]
        if self.p_type == "fire":
            self.not_effective=["fire","water"]
            self.very_effective=[]
        
        elif self.p_type == "water":
            self.not_effective=["water"]
            self.very_effective=["fire"]
        

        
class Pokemon:
    def __init__(self, name, p_type, health, level, moves):
        """
        Initialize a Pokemon object.

        Args:
            name (str): The name of the Pokémon.
            p_type (str): The type of the Pokémon (e.g., 'Water', 'Fire').
            health (int): The health points of the Pokémon.
            level (int): The level of the Pokémon.
            moves (list): A list of Move objects available to the Pokémon.
        """
        self.name=name
        self.p_type=p_type
        self.health=health
        self.level=level
        self.moves=moves


    def attack(self, enemy_pokemon):
        """
        Attack an enemy Pokémon.

        Args:
            enemy_pokemon (Pokemon): The Pokémon being attacked.
        """
        self.enemy_pokemon=enemy_pokemon
        print("0.", self.moves[0].name,"1.", self.moves[1].name,"2.", self.moves[2].name)        
        move=int(input("Select your move: "))
        if self.moves[move].p_type in self.moves[move].not_effective:
            multiplier=0.5
        elif self.moves[move].p_type in self.moves[move].very_effective:
            multiplier=2
        else:
            multiplier=1
        
        damage=int(self.moves[move].damage*self.level*random.random()*multiplier)
        return damage

    
    def receive_damage(self, damage):
        """
        Apply damage to the Pokémon and print its status.

        Args:
            damage (float): The amount of damage received.
        """
        self.damage=damage
        self.health=self.health-self.damage
        if self.health<0:
            print(self.name,"has fainted!")

               
class Arena:
    def __init__(self, arena_name, pokemon1, pokemon2):
        """
        Initialize an Arena object where Pokémon battles take place.

        Args:
            arena_name (str): The name of the arena.
            pokemon1 (Pokemon): The first Pokémon in the battle.
            pokemon2 (Pokemon): The second Pokémon in the battle.
        """
        self.arena_name=arena_name
        self.pokemon1=pokemon1
        self.pokemon2=pokemon2
        
    def fight(self):
        """
        Run a fight between two Pokémon.
        """
        while self.pokemon1.health>0 and self.pokemon2.health >0:
            
            self.pokemon2.receive_damage(self.pokemon1.attack(self.pokemon2))
            
            self.pokemon1.receive_damage(self.pokemon2.attack(self.pokemon1))
            if self.pokemon1.health<0:
                print(self.pokemon2.name, "won!")
                break
            if self.pokemon2.health<0:
                print(self.pokemon1.name, "won!")
                break
            
        
    
def main():
    
    # Create moves for fire:
    ember = Move("Ember", "Fire", 40)
    fiery_dance = Move("Fiery Dance", "Fire", 80)
    blaze_kick = Move("Blaze Kick", "Fire", 85)
    # Create moves for water:
    clamp = Move("Clamp", "Water", 35)
    dive = Move("Dive", "Water", 80)
    bubble_beam = Move("Bubble Beam", "Water", 65)
    
    # Create some Pokémon
    squirtle = Pokemon("Squirtle", "Water", 100, 5, [clamp, dive, bubble_beam])
    charmander = Pokemon("Charmander", "Fire", 90, 4, [ember, fiery_dance, blaze_kick])
    # create the arena
    kanto = Arena("Kanto Gyms", squirtle, charmander)
    kanto.fight()
    
if __name__ == "__main__":
    main()
