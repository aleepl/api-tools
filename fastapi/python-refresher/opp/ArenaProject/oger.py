from enemy import Enemy

class Oger(Enemy):
    def __init__(self, health_points: int=20, attack_damage: int=5):
        super().__init__(type_of_enemy="Oger", 
                         health_points=health_points, 
                         attack_damage=attack_damage)
        
    def talk(self):
        print(f"Oger is slamming hands all around.")