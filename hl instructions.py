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

# main routine
print()
print("⬆️Welcome to Higher or Lower⬇️")
print()

# ask the user if they want instructions (check they say yes/no)
want_instructions = yes_no("Do you want to see the instructions?: ")

#Display the instructions if the user wants to see them
if want_instructions == "yes":
    instructions()

print("program continues")