from colorama import Fore, init
import datetime
import os
import pyperclip
import random
from time import sleep
import socket

init()

__author__ = '0010000000000001'


def ask(question):
    """Waiting for a response"""
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response


def loading():
    print(' Loading.')
    sleep(0.1)
    os.system('cls||clear')
    print(' Loading..')
    sleep(0.4)
    os.system('cls||clear')
    print(' Loading...')
    sleep(0.2)
    os.system('cls||clear')


def main():
    #   PASSWD gen
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    letters += letters.upper()
    symbol = '(!#$/:;<=>?@%*+&,-.~^_€`)'
    letters += symbol
    numbers = '9876543210'
    letters += numbers
    mix = list(letters)
    random.shuffle(mix)

    #   PIN gen
    num = list(numbers)
    random.shuffle(num)

    os.system('MODE CON COLS=49 LINES=10')
    elp = 1
    info = 1

    #   TIME
    now = datetime.datetime.now()
    hour = now.hour

    if hour >= 0 and not hour > 5:
        print('\n Good night,', socket.gethostname())

    elif hour >= 6 and not hour > 11:
        print('\n Good Morning,', socket.gethostname())

    elif hour >= 12 and not hour > 17:
        print('\n Good afternoon,', socket.gethostname())

    elif hour >= 18 and not hour > 23:
        print('\n Good Evening,', socket.gethostname())

    #   PIN
    while True:
        if info == 1:
            print(f'\n{Fore.CYAN} To close the program write: {Fore.RED}exit{Fore.RESET}')
        length = input('\n Password length: ')
        info += 1

        if length == 'exit':
            break

        elif not length.isdigit():
            print(f'{Fore.RED} Only numbers!{Fore.RESET}')

        elif int(length) <= 3:
            print(f'{Fore.RED} Why do you need {length} character(s)?\n Minimum length is 4{Fore.RESET}')

        elif int(length) <= 4 and elp == 1:
            pin = ask('\n Probably you want to create a PIN-CODE? y/n: ')

            if pin == 'y':
                os.system('cls||clear')
                print(f'{Fore.CYAN} After creating a PIN, you can also\n create a password or just close the program {Fore.RESET}')
                pin = ''
                for p in range(int(length)):
                    pin = pin + random.choice(num)
                print(f'\n PIN-code completed: {Fore.YELLOW}{pin}{Fore.RESET}')

                choice = ask('\n Save to txt file? y/n: ')

                if choice == 'y':  # yes

                    use = input('\n Description (example for which device?):\n ')

                    while len(use) > 47:
                        print(f'{Fore.RED} \n PIN-code description takes so much?{Fore.RESET}')
                        use = input(' Description (example for which device?):\n ')

                    with open('my_pass.txt', 'a') as add_password:

                        today = datetime.datetime.today()
                        add_password.write(f'\nTIME: {today.strftime("%d-%m-%Y-%H.%M")}  -  PIN: {pin}  -  {use}')
                        os.system('cls||clear')
                        print(f'{Fore.GREEN} \n PIN-code added successfully, check{Fore.RESET} my_pass.txt')
                        size = os.path.getsize('my_pass.txt')

                        if size == 0:
                            pass

                        elif size >= 61:
                            print(f' New size of the file is {Fore.YELLOW}{size}{Fore.RESET} bytes')

                elif choice == 'n':  # no

                    choice = ask('\n Generate a new password? y/n: ')

                    if choice == 'y':
                        main()

                    elif choice == 'n':
                        print("\n The program will close..")

            elif pin == 'n':
                elp += 1
                pass

        elif int(length) > 25:
            print(f'{Fore.RED} A very strong password is a maximum of 25 chr{Fore.RESET}')

        else:
            break

    #   PASSWD
    new_password = ''
    for p in range(int(length)):
        new_password = new_password + random.choice(mix)
    print(f'\n Password completed: {Fore.YELLOW}{new_password}{Fore.RESET}')

    choice = ask('\n Save to txt file? y/n: ')

    if choice == 'y':  # yes

        use = input('\n Where to be used?:\n ')

        while len(use) > 47:
            print(f'{Fore.RED} \n Password description takes so much?{Fore.RESET}')
            use = input(' Where to be used? (example social networks):\n ')

        with open('my_pass.txt', 'a') as add_password:

            today = datetime.datetime.today()
            os.system('cls||clear')
            add_password.write(f'\nTIME: {today.strftime("%d-%m-%Y-%H.%M")}  -  PASS: {new_password}  -  {use}')
            print(f'{Fore.CYAN} \n There are buffer exchange interceptor programs'
                  f'\n If you are confident in the security\n of your system then click: {Fore.RESET}Y'
                  f'\n\n {Fore.CYAN}If you press{Fore.RESET} N {Fore.CYAN}the clipboard will be cleared{Fore.RESET}')
            # clipboard
            clipboard = ask(f'\n {Fore.RED}[BE CAREFUL] {Fore.RESET}Save password to clipboard? y/n: ')

            if clipboard == 'y':
                loading()
                print(f'{Fore.GREEN} \n Password saved to clipboard for quick use{Fore.RESET}')
                pyperclip.copy(new_password)
                pyperclip.paste()

            elif clipboard == 'n':
                loading()
                empty = ''
                pyperclip.copy(empty)
                pyperclip.paste()

            print(f'{Fore.GREEN} \n Password added successfully, check{Fore.RESET} my_pass.txt')
            size = os.path.getsize('my_pass.txt')

            if size == 0:
                pass

            elif size >= 61:
                print(f' New size of the file is {Fore.YELLOW}{size}{Fore.RESET} bytes')

    elif choice == 'n':  # no
        print(f'{Fore.RED} You refused the password{Fore.RESET}')
        choice = ask('\n Generate a new password? y/n: ')

        if choice == 'y':
            main()

        elif choice == 'n':
            print("\n The program will close..")


if __name__ == '__main__':
    main()
    sleep(6)
