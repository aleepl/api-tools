from enemy import Enemy

class Zombie(Enemy):
    def __init__(self, health_points: int=15, attack_damage: int=3):
        super().__init__(type_of_enemy="Zombie", 
                         health_points=health_points, 
                         attack_damage=attack_damage)
        
    def talk(self):
        print(f"*Grumbling...*")
        
    def spread_disease(self):
        print(f"Zombie spreads disease")