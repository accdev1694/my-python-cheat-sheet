import random

print()
print("Welcome to the RPC game")
print()
play = input("Do you wanna play? y/n: ").lower()
print('---')

if play == 'y':
    name = input("What is your name? ").title()
    print('---')
    count = 0
    player_score = 0
    robot_score = 0
    while count < 10:
        player = input(f"{name}, what is your choice? r/p/s: ").lower()
        print()
        if player in ['r', 'p', 's']:
            robot = random.choice(['r', 'p', 's'])
            
            if (player == 'r' and robot == 's') or (player == 'p' and robot == 'r') or (player == 's' and robot == 'p'):
                count += 1
                player_score += 1
                print(f"<<<-----One for {name}----->>>")
                print()
            elif (robot == 'r' and player == 's') or (robot == 'p' and player == 'r') or (robot == 's' and player == 'p'):
                count += 1
                robot_score += 1
                print("xxx-----One for the ROBOT-----xxx")
                print()
            else:
                print("|||-----Tie-----|||")
                print()
                
                
                
    print('**************')
    print("Game Over!!!")
    if player_score > robot_score:
        print(f"{name} Won!")
        print(f"{name} scored {player_score} points")
        print(f"Robot scored {robot_score} points")
    elif player_score < robot_score:
        print(f"{name} Lost!")
        print(f"{name} scored {player_score} points")
        print(f"Robot scored {robot_score} points")
    else:
        print("Its a tie!")
        print(f"{name} scored {player_score} points")
        print(f"Robot scored {robot_score} points")
    print('**************')
