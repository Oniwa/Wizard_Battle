import random
import time

from actors import Wizard, Creature

def main():
    print_header()
    game_loop()


def print_header():
    print('-----------------------------')
    print('      Wizard Game App')
    print('-----------------------------')
    print()


def game_loop():

    creatures = [
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000),
    ]

    print(creatures)

    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print(f'A {active_creature.name} of {active_creature.level} has appeared'
              f' from a dark and foggy forest...\n')

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover...")
                time.sleep(5)
                print("The wizard returns revitalized!")
        elif cmd == 'r':
            print('The wizard becomes unsure of his power and flees')
        elif cmd == 'l':
            print(f'The wizard {hero.name} takes in the surroundings and sees:')
            for c in creatures:
                print(f' * A {c.name} of level {c.level}')
        else:
            print('OK, exiting game..... bye!')
            break


if __name__ == '__main__':
    main()
