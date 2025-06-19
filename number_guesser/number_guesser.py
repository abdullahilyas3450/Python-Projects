import random 

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    count = 0
    while feedback != 'c':
        count += 1
        guess = random.randint(low, high)
        feedback = input(f'Is the {guess}. Too Low(L || l) OR To High(H || h) or It is Correct(C || c): ').lower()
        if(feedback == 'h'):
            high = guess - 1
        elif(feedback == 'l'):
            low = guess + 1
    print(f'You guessed it right It was {guess} and Number of turns was {count}')

computer_guess(100)