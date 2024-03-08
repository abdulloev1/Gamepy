import random

class Ability:
    def __init__(self, name):
        self.name = name

class Weapon:
    def __init__(self, name, min_damage, max_damage):
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage

class Skill:
    def __init__(self, name):
        self.name = name

class Animal:
    def __init__(self, name):
        self.name = name

class Trap:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Treasure:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Race:
    def __init__(self, name, abilities, weapons, skills, animals, strengths, weaknesses, stamina, combat_spirit, health, animal_health):
        self.name = name
        self.abilities = [Ability(a) for a in abilities]
        self.weapons = [Weapon(w, random.randint(10, 20)) for w in weapons]
        self.skills = [Skill(s) for s in skills]
        self.animals = [Animal(an) for an in animals]
        self.strengths = strengths
        self.weaknesses = weaknesses
        self.stamina = stamina
        self.combat_spirit = combat_spirit
        self.health = health
        self.animal_health = animal_health

class Unit:
    def __init__(self, name, race, x, y):
        self.name = name
        self.race = race
        self.health = race.health
        self.max_health = race.health
        self.stamina = race.stamina
        self.combat_spirit = race.combat_spirit
        self.animal_health = race.animal_health
        self.current_weapon = None
        self.x = x
        self.y = y
        self.experience = 0
        self.level = 1

    def gain_health(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    def lose_health(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def equip_weapon(self, weapon):
        self.current_weapon = weapon

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def receive_experience(self, amount):
        self.experience += amount
        if self.experience >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        self.experience = 0
        print(f"{self.name} leveled up to level {self.level}!")

    def get_damage_multiplier(self, enemy_race):
        if enemy_race.name in self.race.strengths:
            return 1.5  
        elif enemy_race.name in self.race.weaknesses:
            return 0.5  
        else:
            return 1.0  

    def attack(self, enemy):
        if self.current_weapon:
            distance = ((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2) ** 0.5
            if distance <= 1:
                damage = random.randint(self.current_weapon.min_damage, self.current_weapon.max_damage)
                damage *= self.get_damage_multiplier(enemy.race)
                enemy.health -= damage
                if enemy.health <= 0:
                    enemy.health = 0
                return f"{self.name} attacks {enemy.name} with {self.current_weapon.name} causing {damage} damage."
            else:
                return f"{self.name} can't reach {enemy.name} to attack!"
        else:
            return f"{self.name} has no weapon to attack with!"

# Создание рас с уникальными характеристиками
races = {
    "Wizard": Race("Wizard", ["Telekinesis", "Fireball", "Mana Shield"], ["Staff", "Wand"], ["Magic Shield", "Invisibility"],
                   ["Owl", "Dragon"], ["Magic"], ["Physical"], stamina=100, combat_spirit=80, health=120, animal_health=80),
    "Archer": Race("Archer", ["Eagle Eye", "Piercing Shot", "Rain of Arrows"], ["Bow", "Crossbow"], ["Stealth", "Double Shot"],
                   ["Horse", "Wolf"], ["Physical"], ["Magic"], stamina=80, combat_spirit=90, health=100, animal_health=90),
    "Black Mage": Race("Black Mage", ["Dark Arts", "Curse", "Necromancy"], ["Scepter", "Dagger"], ["Shadow Cloak", "Life Drain"],
                       ["Crow", "Snake"], ["Magic"], ["Physical"], stamina=90, combat_spirit=70, health=110, animal_health=70),
    "Knight": Race("Knight", ["Holy Shield", "Charge", "Divine Justice"], ["Sword", "Lance"], ["Valor", "Guardian"],
                   ["Eagle", "Horse"], ["Physical"], ["Magic"], stamina=120, combat_spirit=100, health=150, animal_health=100),
    "Werewolf": Race("Werewolf", ["Bloodlust", "Shapeshift", "Moonlight Howl"], ["Claws", "Fangs"], ["Regeneration", "Savage Roar"],
                     ["Wolf", "Bear"], ["Physical"], ["Magic"], stamina=110, combat_spirit=110, health=130, animal_health=110),
    "Angel": Race("Angel", ["Divine Light", "Heavenly Wrath", "Angelic Blessing"], ["Sword", "Mace"], ["Healing", "Smite"],
                  ["Dove", "Lion"], ["Magic"], ["Physical"], stamina=100, combat_spirit=120, health=140, animal_health=120),
    "Warrior": Race("Warrior", ["Bravery", "Battle Cry", "Rage"], ["Axe", "Hammer"], ["Intimidation", "Berserk"],
                    ["Bear", "Tiger"], ["Physical"], ["Magic"], stamina=130, combat_spirit=80, health=160, animal_health=80)
}

# Создание юнитов
units = [
    Unit("Merlin", races["Wizard"], 3, 4),
    Unit("Legolas", races["Archer"], 7, 6),
    Unit("Gandalf", races["Wizard"], 7, 8),
    Unit("Aragorn", races["Knight"], 6, 3),
    Unit("Saruman", races["Black Mage"], 2, 9),
    Unit("Legion", races["Werewolf"], 1, 1),
    Unit("Artemis", races["Archer"], 9, 4),
    Unit("Michael", races["Angel"], 3, 7),
    Unit("Sylvanas", races["Archer"], 5, 9),
    Unit("Illidan", races["Warrior"], 8, 2),
    Unit("Thrall", races["Warrior"], 1, 5),
    Unit("Tyrande", races["Angel"], 7, 6)
]

# Бои между юнитами разных рас
for i in range(len(units)):
    for j in range(i + 1, len(units)):
        print(units[i].attack(units[j]))
        print(units[j].attack(units[i]))

# Перемещение юнитов
units[0].move_right()
units[1].move_left()
units[2].move_down()
units[3].move_up()

# Получение опыта
units[0].receive_experience(50)
units[3].receive_experience(120)

# Отображение информации о юнитах
for unit in units:
    print(f"{unit.name}: Level {unit.level}, Health {unit.health}/{unit.max_health}, Experience {unit.experience}/{100 * unit.level}")
