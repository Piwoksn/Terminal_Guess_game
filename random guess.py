import random

print('You get the complete Price at first guess.')

def play():
    end = int(input("\n1 to : "))
    guess = random.randint(1, end)
    trial = int(input("How many Trials: "))
    amount = int(input('Trophy Amount to Win: #'))
    print(f'\n___Lucky Win___\nYou only have {trial} trials\n')
    while trial!= 0:
        num = int(input(f'\nGuess a Number from 1 to {end}: '))
        if num == guess:
            print(f'Correct!! guess = {guess}\n You Won #{amount}')
            response = input("\n Reply? Y - Yes | N - No: ")
            if response.lower() == "n":
                print('Byee!')
                break
            else:
                play()
        else:
            amount*=0.80
            print(f'Wrong!!')
            trial-=1
            if trial != 0:
                print(f'\n{trial} more trial  \n \nNew Amount #{amount}')
            else:
                print(f'\nGame Over! lucky guess = {guess}\n You Won = #0')
                response = input("\n Reply? Y - Yes | N - No: ")
                if response.lower() == "n":
                    print('Byee!')
                    break
                else:
                    play()

play()
