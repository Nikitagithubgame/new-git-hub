class User:
    def __init__(self, h = 100, d = 15, n = 'Bob'):
        self.hp = h
        self.dmg = d
        self.name = n
    
    def getname(self):
        try:
            return self.name
        except:
            print("name")
    
    def atak(self, enemy):
        enemy.hp -= self.dmg
        if enemy.hp <= 0:
            print(enemy.name, "kill")
            return True
        print("Осталось у противника", enemy.hp)