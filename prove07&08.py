playagain = 'yes'
while playagain.lower() == 'yes':
    guess_count = 0
    secret = 'radiance'
    guess = ''
    guess = input('What is your guess(you have 10 guesses)? ')
    print('Your hint is: ',end='')
    for i in range(min(len(secret),len(guess))):
        secretsecret = list(secret)
        if secret[i] == guess[i].lower():
            print(guess[i].upper()+' ',end='')
        elif guess[i].lower() in secretsecret:
            print(guess[i].lower()+' ',end='')
        else:
            print('_'+' ',end='')
    print()
    guess_count = guess_count + 1
    
    while secret != guess.lower() :
        while guess_count > 9:
            print('G')
            print('A')
            print('M')
            print('E')
            print(' ')
            print('O')
            print('V')
            print('E')
            print('R')
            print('!')
            guess_count = 0
        else:
            guess = input('What is your guess? ')
            print('Your hint is: ',end='')
            for i in range(min(len(secret),len(guess))):
                secretsecret = list(secret)
                if secret[i] == guess[i].lower():
                    print(guess[i].upper()+' ',end='')
                elif guess[i].lower() in secretsecret:
                    print(guess[i].lower()+' ',end='')
                else:
                    print('_'+' ',end='')
            print()
            guess_count = guess_count + 1
    print()
    print('Nicely Done! You win!')
    print(f'You guessed {guess_count} times')
    playagain = input('Do you want to play again(yes/no)? ')
print()
print('Goodbye then') 
