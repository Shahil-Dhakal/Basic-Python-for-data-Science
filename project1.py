#I am gonna try making a random number generator using python in this for as long as the user wants

print("Welcome to the random number generator:")

def redoo():
    print("Do you want to generate another random number. If 'yes', press 'y' else press any button to quit.")
    decision = input();
    if decision == 'y':
        mainFun()
    else:
        print("Thank You!")


def mainFun():
    print("Please enter the range between which you want to generate a random number:")
    startingRange = input()
    endingRange = input()

    """
    def intCheck():
        if startingRange != int():
            print("You haven given wrong input. Please enter an integer number as an starting range.")
        elif endingRange != int():
            print("You haven given wrong input. Please enter an integer number as an ending range.")
    
    intCheck()
    """


    import random
    print(random.randrange(int(startingRange),int(endingRange)))

    redoo()

mainFun()