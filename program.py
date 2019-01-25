def main():
    print_header()
    game_loop()


def print_header():
    print('-----------------------------')
    print('      Wizard Game App')
    print('-----------------------------')
    print()


def game_loop():
    while True:
        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            print('attack')
        elif cmd == 'r':
            print('run away')
        elif cmd == 'l':
            print('look around')
        else:
            print('OK, exiting game..... bye!')
            break


if __name__ == '__main__':
    main()
