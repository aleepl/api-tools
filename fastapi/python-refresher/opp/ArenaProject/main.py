from enemy import Enemy
from zombie import Zombie
from oger import Oger

def battle(e: Enemy):
    e.talk()
    e.walk_forward()
    e.attack()

# enemy = Enemy("Zombie", 15, 3)
# enemy.__type_of_enemy = "Oger"

# enemy.talk()
# enemy.walk_forward()
# enemy.attack()
# print(enemy.get_type_of_enemy())

# zombie = Zombie(10,1)
# zombie.talk()
# zombie.spread_disease()

# oger = Oger(20,5)
# oger.talk()

zombie = Zombie(10,1)
oger = Oger(20,5)

battle(zombie)
battle(oger)