playground = [3,3,3,0,3,3,3,0]
# index by   [0,1,2,3,4,5,6,7]
"""
      6 5 4
相手7       自分3
      0 1 2
"""

current_player = 1

"""
自分: 1
相手: 2
"""

def winning():
    global current_player
    global playground
    win_condition = [0,0,0]
    if playground[0:3] == win_condition:
        print('Player 1 wins')
        return True
        exit
    if playground[4:7] == win_condition:
        print('Player 2 wins')
        return True
        exit
    return False

def user_input():
    global current_player
    global playground
    user_input_int = int(input()) # allowed choices are 0,1,2 and 4,5,6
    allowed_choice = []
    if current_player == 1:
        allowed_choice = [0,1,2]
    if current_player == 2:
        allowed_choice = [4,5,6]
    while user_input_int not in allowed_choice or playground[user_input_int] == 0:
        print('error')
        user_input_int = int(input())
    return user_input_int

def take_item(): # return True if ends at pos 3 or 7 (free turn)
    global current_player
    global playground
    user_input_choice = user_input()
    current_marble = playground[user_input_choice]
    playground[user_input_choice] = 0
    for i in range(current_marble):
        playground[(user_input_choice+1+i)%8] += 1
    if current_player == 1:
        if (user_input_choice+1+i)%8 in [3,7]:
            current_player = 1
        else:
            current_player = 2
    elif current_player == 2:
        if (user_input_choice+1+i)%8 in [3,7]:
            current_player = 2
        else:
            current_player = 1

def run_game():
    global current_player
    global playground
    print_playground()
    while not winning():
        take_item()
        print_playground()

def print_playground():
    print(f'      {playground[6]} {playground[5]} {playground[4]}\n   {playground[7]}         {playground[3]}\n      {playground[0]} {playground[1]} {playground[2]}')
    print('Current player:', current_player)

run_game()