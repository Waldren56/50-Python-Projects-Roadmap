import sys
from datetime import datetime
import time, os

DIGITS = {
    '0': [
        ' ┏━━━┓ ',
        ' ┃   ┃ ',
        ' ┃   ┃ ',
        ' ┃   ┃ ',
        ' ┗━━━┛ ',
    ],
    '1': [
        '   ┓   ',
        '   ┃   ',
        '   ┃   ',
        '   ┃   ',
        '   ┻   ',
    ],
    '2': [
        ' ┏━━━┓ ',
        '     ┃ ',
        ' ┏━━━┛ ',
        ' ┃     ',
        ' ┗━━━┛ ',
    ],
    '3': [
        ' ┏━━━┓ ',
        '     ┃ ',
        ' ┣━━━┫ ',
        '     ┃ ',
        ' ┗━━━┛ ',
    ],
    '4': [
        ' ┃   ┃ ',
        ' ┃   ┃ ',
        ' ┗━━━┫ ',
        '     ┃ ',
        '     ┻ ',
    ],
    '5': [
        ' ┏━━━┓ ',
        ' ┃     ',
        ' ┗━━━┓ ',
        '     ┃ ',
        ' ┗━━━┛ ',
    ],
    '6': [
        ' ┏━━━┓ ',
        ' ┃     ',
        ' ┣━━━┓ ',
        ' ┃   ┃ ',
        ' ┗━━━┛ ',
    ],
    '7': [
        ' ┏━━━┓ ',
        '     ┃ ',
        '     ┃ ',
        '     ┃ ',
        '     ┻ ',
    ],
    '8': [
        ' ┏━━━┓ ',
        ' ┃   ┃ ',
        ' ┣━━━┫ ',
        ' ┃   ┃ ',
        ' ┗━━━┛ ',
    ],
    '9': [
        ' ┏━━━┓ ',
        ' ┃   ┃ ',
        ' ┗━━━┫ ',
        '     ┃ ',
        ' ┗━━━┛ ',
    ],
    ':': [
        '       ',
        '   ●   ',
        '       ',
        '   ●   ',
        '       ',
    ]
}

def clear():
    """ Checks your operating system and uses the correct clear command """
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    try:
        while True:
            clear()

            print('┏' + '━' * 66 + '┓')
            current_time = datetime.now().strftime('%H:%M:%S')
            for row in range(5):
                print('┃ ', end='')
                for char in current_time:
                    print(DIGITS[char][row], end=' ')

                print(' ┃')
            print('┗' + '━' * 66 + '┛')

            time.sleep(1)

    except KeyboardInterrupt:
        sys.exit("Clock stopped")

if __name__ == "__main__":
    main()