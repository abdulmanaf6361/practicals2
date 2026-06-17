# Build a number guessing game using conditionals and loops:
# •	Set a secret number (e.g. secret = 42).
# •	Use a for loop to give the user 5 attempts.
# •	Each attempt: take input, compare to secret using if/elif/else.
# •	Print 'Too low', 'Too high', or 'Correct! You won in X attempts'.
# •	If all 5 attempts are used without guessing, print 'Game over! The number was 42'.

secret = 42
attempts = 5
while attempts > 0:
    guess = int(input("Enter your guess\n"))
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct! You won in " + str(6 - attempts) + " attempts")
        break
    attempts -= 1
if attempts == 0:
    print("Game over! The number was " + str(secret))