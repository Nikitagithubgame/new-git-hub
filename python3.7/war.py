class User:
    def __init__(self, h = 100, d = 20, n = 'Bob'):
        self.hp = h
        self.dmg = d
        self.name = n
        print("Создан воен.")

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
        while self.dmg < enemy.hp:
            self.hp -= enemy.dmg
        print(self.hp, enemy.hp)


pipol = User()
pipol2 = User()

print("Первый воен:", pipol.hp, pipol.dmg, pipol.name)
print("Второй воен:", pipol2.hp, pipol2.dmg, pipol2.name)

print(pipol.atak(pipol2))
