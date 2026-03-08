# checks for an integer with optional upper /
# lower limits and an optional exit code for infinite mode / quitting the game
def int_check(question, low =None, high=None, exit_code=None):

    # if any integer is allowed
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an integer
    # (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is more"
                 f" than / equal to {low}")

    error = (f"Please enter an integer that"
            f" is between {low} and {high}")


    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check the integer is not too low...
            if low is not None and response < low:
                print(error)
                continue

            # check that the integer is not too high
            if high is not None and response > high:
                print(error)
                continue

            # if response is valid, return it
            else:
                return response

        except ValueError:
            print(error)


# guessing loop

# replace number below with the secret number
secret = 7

# parameters that already exist in the base game
low_num = 0
high_num = 10
guesses_allowed = 5

# set guesses used to zero at the start of each round
guesses_used = 0
already_guessed = []

guess = ""
while guess != secret and guesses_used < guesses_allowed:

    # ask the user to guess the number
    guess = int_check("Guess: ", low_num, high_num, "xxx")

    # check if they want to exit
    if guess == "xxx":
        #set end_game to use so that outer loop can be broken
        end_game = "yes"
        break

     # check that the guess is not a duplicate
    if guess in already_guessed:
        print(f"You've already guessed {guess}. You've *still* used"
                  f" {guesses_used} / {guesses_allowed} guesses")
        continue

        # if guess is not a duplicate, add it to the 'already guessed' list
    else:
        already_guessed.append(guess)

    # add one to the number of guesses used
    guesses_used += 1

    # compare the user's guess with the secret number

    # if we have guesses left
    if guess < secret and guesses_used < guesses_allowed:
        feedback = (f"Too low, please guess a higher number"
                    f" You've used {guesses_used} / {guesses_allowed} guesses")
    elif guess > secret and guesses_used < guesses_allowed:
        feedback = (f"Too high, please guess a lower number"
                    f" You've used {guesses_used} / {guesses_allowed} guesses")

   # when the secret number is guessed have different feedback
    # options (lucky/phew/well done)
    elif guess == secret:

        if guesses_used == 1:
            feedback = "🍀🍀🍀Lucky! You got it on the first guess.🍀🍀🍀 "
        elif guesses_used == guesses_allowed:
            feedback = "Phew! You got it on the last guess. "
        else:
            feedback = (f"Well done! You guessed the secret number "
                        f"in {guesses_used} guesses.")

    # if there are no guesses left
    else:
        feedback = (f"You lost! You failed to guess the secret number "
                    f"in {guesses_allowed} guesses. "
                    f"\nBetter luck next round!")

    #print feedback to user
    print(feedback)

    # additional feedback (warn user they are running out of guesses)
    if guesses_used == guesses_allowed - 1:
        print("\nCareful - you only have 1 guess left!💀💣\n")

print()
print("End of Round")