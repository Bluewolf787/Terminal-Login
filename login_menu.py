from getpass import getpass
from database_helper import save_user, get_key, get_salt, check_username
from hash_helper import hash_password, check_password
import platform
import os


# This function is used to clear the terminal window
def clear_terminal():
    # Get the system name
    system = platform.system()
    if system == 'Linux':
        os.system('clear') # Clear terminal on Linux
    elif system == 'Windows':
        os.system('cls') # Clear terminal on Windows


# Print the main menu
def menu():
    clear_terminal()
    print('Terminal-Login--V1.0.0--Bluewolf787')
    print('=' * 46 + '\n' + '-' * 20 + ' Menu ' + '-' * 20)
    print('''
1. Login
2. Register
Exit. Quit Termianl-Login
    ''')
    print('=' * 46)

    choice = input(': ').lower() # Get input
    while choice != 'exit':
        if choice == '1':
            return login()
        elif choice == '2':
            register()
        else:
            choice = input(': ').lower()
    quit()


# Print login menu
def login():
    clear_terminal()
    print('=' * 46 + '\n' + '-' * 19 + ' Log-In ' + '-' * 19)
    username = input('\nUsername: ') # Get username
    
    # Check if there is a user with the entered username
    user_exits = check_username(username)
    if not user_exits:
        print('\n> There is no user with this username\n\n' + '=' * 46)
        answer = input('Try again? (j/n) or you can quit with exit\n: ').lower()
        while answer != 'exit':
            if answer == 'j':
                login()
            elif answer == 'n':
                menu()
            else:
                answer = input(': ')
        quit()

    plaintext = getpass('Password: ') # Get password

    # Hash entered password with stored salt for this user
    key_to_check = check_password(plaintext, get_salt(username))
    key = get_key(username) # Get the stored key

    if key_to_check == key: # Compare the keys
        logged_in_screen()
    else:
        print('\n> Wrong password\n\n' + '=' * 46)
        answer = input('Try again? (j/n) or you can quit with exit\n: ').lower()
        while answer != 'exit':
            if answer == 'j':
                login()
            elif answer == 'n':
                menu()
            else:
                answer = input(': ')
        quit()


# Print register menu
def register():
    clear_terminal()
    print('=' * 46 + '\n' + '-' * 18 + ' Register ' + '-' * 18)
    username = input('\nEnter a username: ') # Get username

    # Check if there is already a user with the entered username
    user_exits = check_username(username)
    if user_exits:
        print('\n> This username is already taken. Please choose another name\n\n' + '=' * 46)
        answer = input('Continue? (j/n) or you can quit with exit\n: ').lower()
        while answer != 'exit':
            if answer == 'j':
                login()
            elif answer == 'n':
                menu()
            else:
                answer = input(': ')
        quit()

    plaintext = getpass('Enter a password: ') # Get password

    storage = hash_password(plaintext) # Hash password

    save_user(username, storage[32:], storage[:32]) # Store salt and key

    print('\n> New user registered\n\n' + '=' * 46)
    
    answer = input('Do you want to login? (j/n) or you can quit with exit\n: ').lower()
    while answer != 'exit':
        if answer == 'j':
            login()
        elif answer == 'n':
            menu()
        else:
            answer = input(': ')
    quit()


# This function is called when the user is successfuly logged in
def logged_in_screen():
    clear_terminal()
    print('\n> You are now logged in\n')
    answer = input('Quit the program with exit\n: ').lower()
    if answer == 'exit':
        quit() 
    else:
        answer = input(': ')