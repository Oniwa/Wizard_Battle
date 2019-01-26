import random


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return f'Creature {self.name} of level {self.level}'

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):

    def attack(self, creature):
        print(f'The wizard {self.name} attacks {creature.name}!')

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print(f'You roll {my_roll}...')
        print(f'{creature.name} rolls {creature_roll}...')

        if my_roll >= creature_roll:
            print(f'The wizard has handily triumphed over {creature.name}')
            return True
        else:
            print("The wizard has been DEFEATED")
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.breaths_fire = breaths_fire
        self.scaliness = scaliness

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness /10

        return base_roll * fire_modifier * scale_modifier
