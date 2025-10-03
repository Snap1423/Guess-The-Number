import random

def guess_number():
    print("Welcome to the Number guessing!")
    print("I am thinking of a number between 1 to 100")

    # Generate a random number
    secret_number = random.randint(1,100)
    attempt = 0

    while True:
        guess = input("guess the number: ")

        #check valid input
        if not guess.isdigit():
            print("Enter a valid number")
            continue
        guess = int(guess)
        attempt+=1

        if guess < secret_number:
            print("Too low")
        elif guess > secret_number:
            print("too high")
        else:
            print("Congrats🎉🎉 you guessed in ", attempt, "attempts")

# calling the function
guess_number()