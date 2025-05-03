class Character_parms():
    #Определяет параметры персонажей
    def __init__(self, name, level, race):
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def stats(self):
        #вывод параметров персонажа
        description = (self.name + ";" + str(self.level) + ";" + self.race + ";" + str(self.health))
        print(description)

    def level_up(self):
        self.level +=1
        print("У персонажа " + self.name + " новый уровень: " + str(self.level))

# Определяем персонажей:

character1 = Character_parms("Betonich", 4, "Orc")
character2 = Character_parms("Skeleton", 2, "Undead")

# Показать статы персонажа
character1.stats()
character2.stats()

# Поднять уровень персонажу
character1.level_up()

# Проверить статы у персонажа после изменений
character1.stats()