#guess the number
import random
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
numbers = []
for number in range (1, 101):
    numbers.append(number)

print(numbers)
answer = random.choice(numbers)
print(f"Psst the answer is {answer}")

lives = 10
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty_level == "hard":
    lives = 5


end_of_game = False
while not end_of_game:
    if lives == 0:
        end_of_game = True
        print("You've run out of guesses, you lose!")
    elif lives > 0:
        print(f"You have {lives} remaining to guess the number.")
        guess = int(input("Make a guess: "))

    if guess == answer:
        end_of_game = True
        print(f"You got it! The answer is {answer}.")


    elif guess > answer and lives > 0 :
        lives = lives - 1
        print("Too high.")
        print("Guess again.")

    elif guess < answer and lives > 0:
        lives = lives - 1
        print("Too low.")
        print("Guess again.")


