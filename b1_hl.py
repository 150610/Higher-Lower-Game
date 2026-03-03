import math


# checks for an integer more than / equal to 1
def int_check(question, low =None, high=None, exit_code=None):

    # if any integer is allowed
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an integer
    # (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is more"
                 f" than / equal to {low}")

    # if the number needs to be between low & high
    else:
        error =(f"Please enter an integer that"
                f" is between {low} and {high} (inclusive)")

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

            # check the response more than the low number
            elif high is not None and response > low:
                print(error)

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
            print("Please answer yes/no")


def instructions():
    """Prints instructions"""

    print("""
    *** Instructions ****

    Guess the secret number

    """)


# Main routine starts here

# Initialise game variables
mode = "regular"
rounds_played = 0


print("⬆️Welcome to Higher or Lower⬇️")
print()

# Instructions
# ask the user if they want instructions (check they say yes/no)
want_instructions = yes_no("Do you want to see the instructions?: ")

#Display the instructions if the user wants to see them
if want_instructions == "yes":
    instructions()

# Ask the user for the number of rounds/infinite mode
num_rounds = int_check("\nEnter the amount of rounds or press <enter> for infinite: ", low=1, exit_code="")

if num_rounds =="infinite":
    mode = "infinite"
    num_rounds = 5

# get game parameters
low_num = int_check("\nLow Number? ")
high_num = int_check("High Number? ", low=low_num+1)
guesses_allowed = calc_guesses(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds:

    # rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played +1} (Infinite Mode)"
    else:
        rounds_heading = f"\n Round {rounds_played +1} of {num_rounds}"

    print(rounds_heading)
    print()

    # get user choice
    user_choice = input("Choose: ")

    # if user choice is the exit code, break the loop
    if user_choice =="xxx":
        break

    rounds_played +=1


    # if users are in infinite mode add more rounds
    if mode == "infinite":
        num_rounds += 1



# Game history/ statistics area