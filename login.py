from random import choice
from time import sleep
import string


# ps and pas are short terms for password
def password(ps):
    tries = 0
    user_password = input('Enter your password here: ')
    if user_password == ps:
        return 'login_complete'
    print('Incorect password!')
    while tries < 4:
        user_password2 = input('Enter password: ')
        if user_password2 == ps:
            return 'login_complete'
        print('Incorect password!')
        tries += 1

        # set the amount of tries the user has
        if tries == 4:
            return 'login_failed'


# password generator
def generate_password():
    all_letters = string.ascii_letters + string.digits + string.punctuation

    while True:
        password_lenght = input('Password lenght: ')
        invalid_amount = 0

        # checking if the input is valid
        for character in password_lenght:
            if character in string.digits:
                pass
            else:
                print('Invalid amount')
                invalid_amount += 1
                break

        # generating the password
        if invalid_amount == 0:
            password = ''
            for time in range(1, int(password_lenght)):
                password += ''.join(choice(all_letters))

            print(f'Generated password: {password}')
            break


# improved version of Juni's countdown (Juni Learning (YouTube))
def countdown(t):
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        sleep(1)
        t -= 1


unlock = False

# you can change the name and password to your own
name = 'Coder'
pas = '7G'

# you can add your own funny messages
funny_message = ['wow', 'ok', 'nice try', 'so close', 'really?']

# the amount of tries
count = 0

# checking if the input is valid
while True:
    user_choice = input(
        'What do you want to do? (Generate a strong random password (type: GP) OR Log in(type: LI)) ')
    if user_choice == 'LI' or user_choice == 'GP':
        break
    else:
        print('Invalid command')

if user_choice == 'LI':
    while True:

        # the amount of allowed tries
        if count == 5:
            print('Login Failed!')
            break
        login = password(pas)
        if login == 'login_complete':
            unlock = True
            print(f'Welcome back {name}!')
            break
        if login == 'login_failed':
            print('Login Failed!')
            print(choice(funny_message))
            sleep(2)
            print('You can try again after:')

        # set your own countdown duration by changing the value of time in secundes
            time = 180
            countdown(time)

            count += 1

if user_choice == 'GP':
    while True:
        generate_password()
        quit = input('End program? (y/n)')
        if quit == 'y':
            break
