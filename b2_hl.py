import math
import random

# checks for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
def int_check(question, low =None, high=None, exit_code=None):

    # if any integer is allowed
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an integer
    # (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is more"
                 f" than or equal to {low}")

    # if the number needs to be between low & high
    else:
        error =(f"Please enter an integer that"
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

            # check the response more than the high number
            elif high is not None and response > high:
                print(error)
                continue

            # if response is valid, return it
            else:
                return response

        except ValueError:
            print(error)

# calculate the number of guesses allowed
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses

# checks a user enters yes/no
def yes_no(question):
    """Checks user response to a question in y/n, returns 'yes' or 'no '"""

    while True:

        response = input(question).lower()

        # check if the user says yes/no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("\nPlease answer yes/no")


def instructions():
    """Prints instructions"""

    print("""
    *** Instructions ****
    
    Choose the amount of rounds you would like to play 
    (Or play infinite mode)
    
    Then set a low number and a high number, this is your number range 
    
    You have to guess the 'secret' number within your chosen range 
    (This includes the high and low numbers!)
    
    Try to find out the secret number in the fewest guesses for a better score

    """)


# Main routine starts here

# Initialise game variables
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""
default_params ="no"
score = 0

game_history = []
all_scores = []

print("⬆️Welcome to Higher or Lower⬇️")
print()

# Instructions
# ask the user if they want instructions (check they say yes/no)
want_instructions = yes_no("Do you want to see the instructions?: ")

#Display the instructions if the user wants to see them
if want_instructions == "yes":
    instructions()

# Ask the user for the number of rounds/infinite mode
num_rounds = int_check("\nEnter the amount of rounds or press <enter> for infinite: ",
                       low=1, exit_code="")

if num_rounds =="":
    mode = "infinite"
    num_rounds = 5

# ask the user if they want to customize the number range
default_params = yes_no("\nThe default number range is 0 - 10"
                        "\nDo you want to use the default number range?  ")

if default_params == "yes":
    low_num = 0
    high_num = 10

# allow user to choose the high / low number
else:
    low_num = int_check("\nLow Number? ")
    high_num = int_check("High Number? ", low=low_num+1)

# calculate the maximum number of guesses based on the low and high number
guesses_allowed = calc_guesses(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds:

    # rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played +1} (Infinite Mode)"
    else:
        rounds_heading = f"\n Round {rounds_played +1} of {num_rounds}"

    print(rounds_heading)

    # round starts here
    # set guesses used to zero at the start of each round
    guesses_used = 0
    already_guessed = []

    # choose a 'secret' number between the low and high numbers
    secret = random.randint(low_num, high_num)
    #print("spoiler", secret) # REMOVE THIS WHEN DONE TESTING

    guess = ""
    while guess != secret and guesses_used < guesses_allowed:

        # ask the user to guess the number
        guess = int_check("Guess: ", low_num, high_num, "xxx")

        # check if they want to exit
        if guess == "xxx":
            # set end_game to use so that outer loop can be broken
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

        # additional feedback (warn user they are running out of guesses)
        if guesses_used == guesses_allowed - 1 and guess is not secret:
            print("\nCareful - you only have 1 guess left!💀💣\n")

        # when the secret number is guessed have different feedback
        # options (lucky/phew/well done)
        if guess == secret:

            if guesses_used == 1:
                feedback = "🍀🍀🍀Lucky! You got it on the first guess.🍀🍀🍀 "
                score = 1
            elif guesses_used == guesses_allowed:
                feedback = "Phew! You got it on the last guess. "
            else:
                feedback = (f"Well done! You guessed the secret number "
                            f"in {guesses_used} guesses.")


        # if there are no guesses left
        elif guesses_used == guesses_allowed:
            feedback = (f"You lost! You failed to guess the secret number "
                        f"in {guesses_allowed} guesses. "
                        f"\nBetter luck next round!")


        if guesses_used == guesses_allowed and guess is not secret:
            guesses_used = guesses_allowed + 1
        score = guesses_used

        # print feedback to user
        print(feedback)

    print()

    # round ends here

    # if user has entered the exit code end the game!!
    if end_game == "yes":
        break

    rounds_played +=1
    # if users are in infinite mode add more rounds
    if mode == "infinite":
        num_rounds += 1

    # add round result to game history
    history_feedback = f"Round: {rounds_played}     Score: {score}"
    all_scores.append(score)
    game_history.append(history_feedback)

# check users have played at least 1 round before calculating stats
if rounds_played > 0:
    # game history / stats area
    # calculate statistics
    all_scores.sort()
    best_score = all_scores[0]
    worst_score = all_scores [-1]
    average_score = sum(all_scores) / len(all_scores)

    # print("worst score",worst_score)
    # print("best score",best_score)
    # print("all scores", all_scores)
    # print("length scores", len(all_scores))


    # display the game history on request
    # ask the user if they want to see their game history and output if answer is yes
    see_history = yes_no("\nDo you want to see your game history? ")
    if see_history == "yes":

        # game history
        print("\n📜📜📜Game History📜📜📜")
        print()
        for item in game_history:
            print(item)

        # output the statistics
        print("\n📊📊📊 Statistics 📊📊📊")
        print(f"\nLeast Guesses: {best_score} | Most Guesses: {worst_score} | Average Guesses: {average_score:.2f}")
        print()

        print("Thanks for playing!")