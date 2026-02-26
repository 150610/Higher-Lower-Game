# checks for an integer more than / equal to 1
def int_check(question):
    while True:
        error = "Please enter an integer more than / equal to 1"

        to_check = input(question)

        # check for infinite mode
        if to_check =="":
            return "infinite"

        try:
            response = int(to_check)

            #checks that the number is more than/equal to 1
            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


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
num_rounds = int_check("How many rounds would you like to play? Press <enter> for infinite mode: ")

if num_rounds =="infinite":
    mode = "infinite"
    num_rounds = 5

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