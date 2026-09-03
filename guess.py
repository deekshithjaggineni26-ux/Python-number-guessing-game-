import random

while True:

    number = random.randint(1, 100)

    print("\n🎯 Number Guessing Game")
    print("I have selected a number between 1 and 100")

    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == number:
                print("🎉 Correct! You guessed the number!")
                print("Attempts:", attempts)
                break

            elif guess < number:
                print("Too Low!")

            else:
                print("Too High!")

            print("Attempts left:", max_attempts - attempts)

        except ValueError:
            print("Please enter numbers only!")

    else:
        print("Sorry! You used all 5 attempts.")
        print("The number was:", number)

    again = input("\nDo you want to play again? (yes/no): ")

    if again.lower() != "yes":
        print("Thanks for playing! 👋")
        break