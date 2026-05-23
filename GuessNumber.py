import random

wins = 1
max = 100

answer = 0
lives = -1

print("\nGuess the Number! (1-100)\n\nWrite '-1' to stop")

while True:

    chosen_number = random.randint(1, max * wins)

    difficulty = int(input("What difficulty would you like?\nEasy (1): Unlimited Guesses\nHard (2): Only 5 Guesses\n>>> "))

    if difficulty == 2:
        print("Hard Difficulty has been Chosen!")
        lives = 5
    else:
        print("Easy Difficulty has been Chosen!")

    while answer != "-1":

        answer = input(f"(1-{max*wins}) >>> ")

        if not answer.isdigit() and answer != "-1":
            print("Invalid Input Format! Make sure to Input an Integer")
            continue

        if int(answer) == chosen_number:
            print("Correct!")
            wins += 1
            break
        elif int(answer) > chosen_number:
            print("Too high!")
            lives -= 1
            if lives == 0:
                print("Game over!")
                break
        else:
            print("Too low")
            lives -= 1
            if lives == 0:
                print("Game over!")
                break

        if lives > -1: print(f"Remaining lives: {lives}")

    answer = input("Try again? (y/n)\n>>> ")

    if answer != 'y':
        print("Bye")
        break