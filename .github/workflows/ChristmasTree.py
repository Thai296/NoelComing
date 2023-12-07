import os
import random
from time import sleep

def print_frame(width):
    print('+' + '-' * width + '+')

def random_white_star():
    return '\033[1;37m*\033[0m' if random.random() < 0.1 else '\033[1;30m*\033[0m'

def print_tree_top():
    colors = ['\033[1;31m', '\033[33m', '\033[1;34m']
    color = random.choice(colors)
    print(color, (' ' * 6) + 'Merry Christmas! 2023')
    print(color, (' ' * 13) + 'NY <3')
    color = random.choice(colors)
    print(color, (' ' * 15) + '*')
    print(color, (' ' * 10) + '*  *' + (' ' * 3 + '*  *'))
    print(color, (' ' * 13) + '*   *')
    print(color, (' ' * 11) + '*       *')

def print_tree(height):
    colors = ['\033[1;31m', '\033[33m', '\033[1;34m']
    for i in range(height):
        print(' ' * (height - i), end='')
        for j in range((2 * i) + 1):
            if random.random() < 0.1:
                color = random.choice(colors)
                print(color, end='')
            else:
                print('\033[32m', end='')
            print('*', end='')
        print()

    print((' ' * (height - 1)) + '<<T>>')
    print((' ' * (height - 1)) + '<<<<3')
    print((' ' * (height - 1)) + '<<Y>>')

def print_tree_bottom():
    color = random.choice(['\033[1;31m', '\033[33m', '\033[1;34m'])
    print(color + (' ' * 8) + '_$$$$$$$$$$$$$$$$$_' + '\033[0m')
    print(color + (' ' * 8) + '_$$$$$$$$$$$$$$$$$_' + '\033[0m')

def christmas_tree(height):
    frame_width = height * 2 + 3
    print_frame(frame_width)

    print_tree_top()
    print_tree(height)
    print_tree_bottom()

    print_frame(frame_width)

for i in range(100):
    christmas_tree(16)
    sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
