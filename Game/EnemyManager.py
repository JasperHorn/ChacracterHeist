
class EnemyManager:
    def __init__(self):
        self.enemies = []

    def addEnemy(self, enemy):
        self.enemies.append(enemy)

    def move(self):
        for enemy in self.enemies:
            enemy.move()
