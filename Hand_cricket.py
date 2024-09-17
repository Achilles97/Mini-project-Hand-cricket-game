import random

toss_list = ['H', 'T']
num_list = ['1', '2', '3', '4', '5', '6']
choice_list = ['Bat', 'Bowl']
Bat_score = 0
Ball_score = 0

# Function for batting
def bat():
    global Bat_score
    while True:
        num = input('Enter a number between 1 to 6. To stop, enter "dec": ')
        if num == 'dec':
            print(f'You have declared 👏🏻👏🏻👏🏻.\nYour score is {Bat_score}.')
            break
        try:
            num = int(num)
            if 1 <= num <= 6:
                comp_num = random.randint(1, 6)
                if num == comp_num:
                    print(f'Sorry, you are out.\nYour total score is {Bat_score}.')
                    break
                else:
                    Bat_score += num
                    if num == 6 or num == 4:
                        print(f'You have scored a boundary 🎊🎊, {num} runs.')
                    else:
                        print(f'You scored {num} runs.')
            else:
                print('Invalid input, please enter a valid number between 1 and 6.')
        except ValueError:
            print('Invalid input, please enter a valid number between 1 and 6.')

# Function for bowling
def bowl():
    global Ball_score
    while True:
        num = input('Enter a number between 1 to 6. To stop, enter "dec": ')
        if num == 'dec':
            print(f'You have declared. The computer score is {Ball_score}.')
            break
        try:
            num = int(num)
            if 1 <= num <= 6:
                comp_num = random.randint(1, 6)
                if num == comp_num:
                    print('Congrats, you got a wicket 🙌🙌.')
                    break
                else:
                    Ball_score += comp_num
                    print(f'Computer scored {comp_num} runs.')
            else:
                print('Invalid input, please enter a valid number between 1 and 6.')
        except ValueError:
            print('Invalid input, please enter a valid number between 1 and 6.')

# Main game code
user_name = input('Welcome to hand cricket 🏏! Enter your name: ')
user_toss = input('Ready for the toss 🪙? Choose between heads (H) and tails (T): ').upper()
toss = random.choice(toss_list)

if user_toss == toss:  # Coin toss
    user_choice = input('Bat or Bowl 🏏: ').lower()
    if user_choice == 'bat':
        print(f'{user_name} chose to bat.')
        bat()  # Calling bat function
        print('End of the first innings.')
        print(f'Computer needs {Bat_score + 1} to win.')
        bowl()
        if Ball_score >= Bat_score:
            print(f'Computer wins by {Ball_score - Bat_score} runs!')
        else:
            print(f'{user_name} wins by {Bat_score - Ball_score} runs!')
    else:
        print(f'{user_name} chose to bowl.')
        bowl()  # Calling bowl function
        print('End of the first innings.')
        print(f'{user_name} needs {Ball_score + 1} to win.')
        bat()
