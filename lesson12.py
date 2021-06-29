import random

print('hello, what is your name?')
name = input()
secretnumber = random.randint(1,20)
print(f'well {name}, I have the number in mind, can you guess between 1 to 20?')


for guesses in range(1,7):
        print('take a guess')
        guess = int(input())
        if guess < secretnumber:
            print('your guess is too low')
        elif guess > secretnumber:
            print('your guess is too high')
        else:
            break #if the answer is correct, it will get out from the loop and print next if condition 
    
if guess == secretnumber:
    print(f'you guessed it right {name}')
else:
    print('sorry, your round is over')    