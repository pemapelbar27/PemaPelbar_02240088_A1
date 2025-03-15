import random 
while True:
    print('1. Number guess game')
    print('2.Rock Paper Scisors game')
    print('Press 0 to EXIT')
    user_choice = input("Play the one you like:")
    if user_choice == '1':
        def num_guess_game():
            computer = random.randint(1,100)
            print(f"Try your luck")
            print(f"Guess any num between 1-100")

            while True:
                choice = int(input("Enter your guess:"))
                if choice < computer :
                    print('Estimate upward')
                elif choice > computer :
                    print('Estimate downward')
                else:
                    print('Bravo, you did it')
                    user_choice = input('You want to continue?(Y/N):').upper()
                    if user_choice == 'N': break
    
                
        num_guess_game()
    elif user_choice == '0':
        break
    else:
        def rock_paper_scissors_game():
            your_choice = ['rock', 'paper', 'scissor']
            print('Welcome to Roshambo')
            while True:
                your_choice = input("Enter rock, paper or scissor:").lower()
                comp_choice =random.choice(your_choice)
                print(f'Comp choice:{comp_choice}')
                if your_choice == comp_choice:
                    print('Its draw')
                elif (user_choice == 'rock' and comp_choice == 'scissors'):
                    (user_choice == 'paper' and comp_choice == 'rock')
                    (user_choice == 'scissors' and comp_choice == 'rock')
                    print('You won')
                else:
                    print('Defeated')
                choose =input('One more round? Y/N:').upper()
                if choose == ('N'): break
        
        rock_paper_scissors_game()