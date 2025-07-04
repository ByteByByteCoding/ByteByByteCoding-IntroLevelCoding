import random

def greeting():
    print("Welcome to Guess the Number!")
    print("I will pick a number (whole number), and you will have to guess it!")
    print("I will indicate whether your guess is too high or too low!")

def game(lower_bound, upper_bound):
    print(f"I am thinking of a number from {lower_bound}-{upper_bound}")
    guess_number = random.randint(lower_bound, upper_bound)
    user_guess = 0
    attempts = 0
    while user_guess != guess_number:
        attempts += 1
        user_guess = int(input(f"Enter a guess ({lower_bound}-{upper_bound}): "))
        if user_guess > guess_number:
            print("Try Again! That number was high.")
        if user_guess < guess_number:
            print("Try Again! That number was low.")
    print(f"You got it! It was {guess_number}!")
    print(f"It took you {attempts} attempt(s)!")

def main():
    greeting()
    upper_bound = int(input("What is the upper bound? (To what number would you like to guess?) "))
    lower_bound = int(input("What is the lower bound? (From what number would you like to guess?) "))
    game(lower_bound, upper_bound)
    
if __name__ == "__main__":
    main()
