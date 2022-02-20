from colorama import Fore, init
import datetime
import os
import pyperclip
import random
from time import sleep

init()

__author__ = '0010000000000001'


def ask(question):
    """Waiting for a response"""
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response


def main():
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    letters += letters.upper()
    symbol = '(!#$/:;<=>?@%*+&,-.~^_€`)'
    letters += symbol
    numbers = '9876543210'
    letters += numbers
    mix = list(letters)
    random.shuffle(mix)

    os.system('MODE CON COLS=48 LINES=10')

    length = input('\n Password length: ')

    while True:

        if not length.isdigit():
            print(f'{Fore.RED} Only numbers!{Fore.RESET}')

        elif int(length) <= 3:
            print(f'{Fore.RED} Minimum length is 4{Fore.RESET}')

        elif int(length) > 20:
            print(f'{Fore.RED} Maximum length is 20{Fore.RESET}')

        else:
            break

        length = input('\n Password length: ')

    new_password = ''
    for p in range(int(length)):
        new_password = new_password + random.choice(mix)
    print(f'\n Password completed: {Fore.YELLOW}{new_password}{Fore.RESET}')

    choice = ask('\n Save to txt file? y/n: ')

    if choice == 'y':   # yes

        pyperclip.copy(new_password)
        pyperclip.paste()
        print(f'{Fore.GREEN} Password saved to clipboard for quick use{Fore.RESET}')
        use = input('\n Where to be used?: ')

        while len(use) > 28:

            print(f'{Fore.RED} Maximum length!{Fore.RESET}')
            use = input('\n Where to be used?: ')

        with open('yr_pass.txt', 'a') as add_password:

            today = datetime.datetime.today()
            add_password.write(f'\nTIME: {today.strftime("%d-%m-%Y-%H.%M")}  -  PASS: {new_password}  -  {use}')
            print(f'{Fore.GREEN} Password added successfully, check{Fore.RESET} yr_pass.txt')
            size = os.path.getsize('yr_pass.txt')
            
            if size == 0:
                pass

            elif size >= 61:
                print(f' New size of the file is {Fore.YELLOW}{size}{Fore.RESET} bytes')

    elif choice == 'n':   # no
      
        choice = ask('\n Generate a new password? y/n: ')

        if choice == 'y':
            main()

        elif choice == 'n':
            print("\n The program will close after 6 seconds")


if __name__ == '__main__':
    main()
    sleep(6)
