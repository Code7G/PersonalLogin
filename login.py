from random import choice
import time


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
        if tries == 4:
            return 'login_failed'


# improved version of Juni's countdown(Juni Learning (YouTube))
def countdown(t):
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


unlock = False

# you can change the name and password to your own
name = 'Coder'
pas = '7G'

# you can add your own funny messages
funny_message = ['wow', 'ok', 'nice try', 'so close', 'really?']
# 1
login = (password(ps=pas))
if login == 'login_complete':
    unlock = True
    print(f'Welcome back {name}!')
elif login == 'login_failed':
    print('Login Failed!')
    print(choice(funny_message))
    time.sleep(3)
    print('You can try again after:')

# set your own countdown duration by changing the value of t in secundes
    t = 180
    countdown(t)
#                                    # 2
# after this you can add as many tries as you want by copying the code from #1 to #2 without the # line
    login = (password(ps=pas))
    if login == 'login_complete':
        unlock = True
        print(f'Welcome back {name}!')
    elif login == 'login_failed':
        print('Login Failed!')
        print(choice(funny_message))
        time.sleep(2)
        print('No more tries!')
