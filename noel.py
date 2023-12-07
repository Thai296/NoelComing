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
    print(color, (' ' * 15) + 'Merry Christmas! 2023')
    print(color, (' ' * 23) + 'NY <3')
    color = random.choice(colors)
    print(color, (' ' * 25) + '*')
    print(color, (' ' * 20) + '*  *' + (' ' * 3 + '*  *'))
    print(color, (' ' * 23) + '*   *')
    print(color, (' ' * 21) + '*       *')
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
    print((' ' * (height - 1)) + '<<Y>>')
    # print((' ' * (height - 1)) + 'mWm')
    # print((' ' * (height - 1)) + 'mWm')
    # print(color + (' ' * 16) + '$$$$$$$$$$$$$$$$$$$$$' + '\033[0m')
    print(color + (' ' * 16) + '$$$$$$$$$$$$$$$$$$$$$$' + '\033[0m')
    # print_frame(frame_width)
while True:
    christmas_tree(26)
    sleep(0.5)
    # os.system('cls')
1