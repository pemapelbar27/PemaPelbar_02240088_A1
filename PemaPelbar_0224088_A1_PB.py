import random
#main game menu list 
while True:
    #display menu option
    print('1. Number guess game')
    print('2.Rock Paper Scisors game')
    print('Press 0 to EXIT')
    user_choice = input("Play the one you like:")
    if user_choice == '1':
        #number guessing game function
        def num_guess_game():
            #computer to generate random numbers
            computer = random.randint(1,100)
            print(f"Try your luck")
            print(f"Guess any num between 1-100")

            while True:
                #get users guess
                choice = int(input("Enter your guess:"))
                #compare users guess with computer
                if choice < computer :
                    print('Estimate upward')
                elif choice > computer :
                    print('Estimate downward')
                else:
                    print('Bravo, you did it')
                    #ask if they want to play again
                    user_choice = input('You want to continue?(Y/N):').upper()
                    if user_choice == 'N': break
    
          #call number guessing game function      
        num_guess_game()
    elif user_choice == '0':
        break
    else:
        #rock paper sicssors game fucntion
        def rock_paper_scissors_game():
            your_choice = ['rock', 'paper', 'scissor']
            #list of valid option
            print('Welcome to Roshambo')
            while True:
                #get user"s choice
                your_choice = input("Enter rock, paper or scissor:").lower()
                comp_choice =random.choice(your_choice)
                print(f'Comp choice:{comp_choice}')
                #determine winner
                if your_choice == comp_choice:
                    print('Its draw')
                elif (user_choice == 'rock' and comp_choice == 'scissors'):
                    (user_choice == 'paper' and comp_choice == 'rock')
                    (user_choice == 'scissors' and comp_choice == 'rock')
                    print('You won')
                else:
                    print('Defeated')
                    #ask if user want to play another round
                choose =input('One more round? Y/N:').upper()
                if choose == ('N'): break
        #call function
        rock_paper_scissors_game()
