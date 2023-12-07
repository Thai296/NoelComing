import os
import random
from os import system
from time import sleep

def print_frame(width):
    print('+' + '-' * width + '+')

def random_white_star():
    if random.random() < 0.1:
        return '\033[1;37m*\033[0m'  # White color for blinking stars
    else:
        return '\033[1;30m*\033[0m'  # Green color for non-blinking stars

def christmas_tree(height):
    frame_width = height * 2 + 3  # Adjust the frame width as needed
    print_frame(frame_width)
    # print('\n')
    colors = ['\033[1;31m', '\033[33m', '\033[1;34m']
    color = random.choice(colors)
    print(color, (' ' * 6) + 'Merry Christmas! 2023')
    print(color, (' ' * 13) + 'NY <3')
    color = random.choice(colors)
    print(color, (' ' * 15) + '*')
    print(color, (' ' * 10) + '*  *' + (' ' * 3 + '*  *'))
    print(color, (' ' * 13) + '*   *')
    print(color, (' ' * 11) + '*       *')
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
    print(color + (' ' * 8) + '_$$$$$$$$$$$$$$$$$_' + '\033[0m')
    print(color + (' ' * 8) + '_$$$$$$$$$$$$$$$$$_' + '\033[0m')
    print_frame(frame_width)
i = 1
while True:
    christmas_tree(16)
    sleep(0.1)
    os.system("cls")
    i = i + 1
    if i > 100:
        break
1
# for i in range(20):
#     christmas_tree(26)
#     sleep(0.5)
#     os.system('cls')
