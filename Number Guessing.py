import random
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    lower_bound = int(input("Enter the lower bound of the range:"))
    upper_bound = int(input("Enter the upper bound of the range:"))
    secret_number = random.randint(lower_bound, upper_bound)
    max_attempts = int(input("Enter the maximum number of attempts:"))
    attempts = 0
    while attempts < max_attempts:
        guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}:"))
        attempts += 1
        if guess < secret_number:
            print("Try Again! Your guess was too low.")
        elif guess > secret_number:
            print("Try Again! Your guess was too high.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break
    else:
        print(f"Better Luck Next Time! The number was {secret_number}.")

#Run the game
if __name__ == "__main__":
    number_guessing_game()
