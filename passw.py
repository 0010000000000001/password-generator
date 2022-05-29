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


def main():
    #   PASSWD
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    letters += letters.upper()
    symbol = '(!#$/:;<=>?@%*+&,-.~^_€`)'
    letters += symbol
    numbers = '9876543210'
    letters += numbers
    mix = list(letters)
    random.shuffle(mix)

    #   PIN
    num = list(numbers)
    random.shuffle(num)

    os.system('MODE CON COLS=48 LINES=10')
    elp = 1
    info = 1
    
    #   TIME
    now = datetime.datetime.now()
    hour = now.hour

    if hour > 0 and hour <= 6:
        print(' Good Morning,', socket.gethostname())

    elif hour > 6 and hour <= 12:
        print(' Good afternoon,', socket.gethostname())

    elif hour > 12 and hour <= 18:
        print(' Good Evening,', socket.gethostname())

    elif hour > 18 and hour < 23:
        print(' Good Night,', socket.gethostname())

    while True:
        if info == 1:
            print(f'\n{Fore.CYAN} To close the program,\n you can always write: {Fore.RED}exit{Fore.RESET}')
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
                print(f'{Fore.CYAN} After creating a PIN, you can also\n create a password or just close the program {Fore.RESET}')
                pin = ''
                for p in range(int(length)):
                    pin = pin + random.choice(num)
                print(f'\n PIN-code completed: {Fore.YELLOW}{pin}{Fore.RESET}')

                choice = ask('\n Save to txt file? y/n: ')

                if choice == 'y':  # yes

                    pyperclip.copy(pin)
                    pyperclip.paste()
                    print(f'{Fore.GREEN} PIN-code saved to clipboard for quick use{Fore.RESET}')
                    use = input('\n Description (example for which device?):\n ')

                    while len(use) > 47:
                        print(f'{Fore.RED} PIN-code description takes so much?{Fore.RESET}')
                        sleep(1)
                        os.system('cls')
                        use = input('\n Description (example for which device?):\n ')

                    with open('my_pass.txt', 'a') as add_password:

                        today = datetime.datetime.today()
                        add_password.write(f'\nTIME: {today.strftime("%d-%m-%Y-%H.%M")}  -  PIN: {pin}  -  {use}')
                        print(f'{Fore.GREEN} PIN-code added successfully, check{Fore.RESET} my_pass.txt')
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
                        print("\n The program will close after 6 seconds")

            elif pin == 'n':
                elp += 1
                pass

        elif int(length) > 20:
            print(f'{Fore.RED} A very strong password is \n a maximum of 20 characters{Fore.RESET}')

        else:
            break

    new_password = ''
    for p in range(int(length)):
        new_password = new_password + random.choice(mix)
    print(f'\n Password completed: {Fore.YELLOW}{new_password}{Fore.RESET}')

    choice = ask('\n Save to txt file? y/n: ')

    if choice == 'y':  # yes

        pyperclip.copy(new_password)
        pyperclip.paste()
        print(f'{Fore.GREEN} Password saved to clipboard for quick use{Fore.RESET}')
        use = input('\n Where to be used?: ')

        while len(use) > 47:
            print(f'{Fore.RED} Password description takes so much?{Fore.RESET}')
            sleep(1)
            os.system('cls')
            use = input('\n Where to be used? (example social networks): ')

        with open('my_pass.txt', 'a') as add_password:

            today = datetime.datetime.today()
            add_password.write(f'\nTIME: {today.strftime("%d-%m-%Y-%H.%M")}  -  PASS: {new_password}  -  {use}')
            print(f'{Fore.GREEN} Password added successfully, check{Fore.RESET} my_pass.txt')
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
    sleep(4)
