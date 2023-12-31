import random

def randomIntegerGenerator(min, max):
    """
    This function returns a random integer within the min and max range,
    
    Args:
        min (int): The minimum range for the integers to be generated,
        max (int): The maximum range for the integers to be generated.
        
    Returns:
        int: A random integer between the min and max.
    """
    
    # trying to convert the input operands to ints if not possible
    # query user for new inputs
    try:
        min = int(min)
        max = int(max)
    except ValueError:
        print("Invalid input! Please enter valid integer values.")
        min = int(input("Enter the minimum range: "))
        max = int(input("Enter the maximum range: "))
        
    return random.randint(min, max)

def randomOperationSelector():
    """
    This function randomly returns one of the mathematical operators out 
    of: '+', '-', '*'
    
    Returns:
        str: Randomly choosen mathematical operator
    """
    
    # make random selection out of the 3 opertors and return it
    return random.choice(['+', '-', '*'])


def performMathOperation(n1, n2, o):
    """
    This function can be used to perform a mathematical operation 
    ('+', '-', '*') on two numbers.
    
    Arg:
        n1 (int/float): The first operands,
        n2 (int/float): The second operand,
        o (str): The operator which needs to be applied on the operands.
        
    Returns:
        p (str): string denoting the opertion on the operands,
        a (int/float): result of the operation on the operands.
    """
    
    # trying to convert the input operands to floats if not possible
    # query user for new inputs
    try:
        n1 = float(n1)
        n2 = float(n2)
    except ValueError:
        print("Invalid input! Please enter valid integer/float values.")
        n1 = float(input("Enter the first operand: "))
        n2 = float(input("Enter the second operand: "))
    
    if o not in ['+', '-', '*']:
        o = input("You can only choose o from '+', '-', '*', \
                  please choose properly: ")
        
    # create a string for the opeartion to be carried out
    p = f"{n1} {o} {n2}"
    
    # carry out the operation o on the operands n1 and n2
    if o == '-': a = n1 - n2
    elif o == '+': a = n1 + n2
    else: a = n1 * n2
        
    return p, a

def math_quiz():
    """
    This function is used to emulate a mathematical quiz game. The player is asked questions and if
    she gives correct answers, she earns a point.
    
    Return:
        None
    """
    s = 0                                           # initialize the score variable
    t_q = 10

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        # generate random numbers and an operator
        n1 = randomIntegerGenerator(1, 10);
        n2 = randomIntegerGenerator(1, 5.5);
        o = randomOperationSelector()

        # perform math operation and get the correct answer
        PROBLEM, ANSWER = performMathOperation(n1, n2, o)
        
        # display the question 
        print(f"\nQuestion: {PROBLEM}")
        
        # get the user's answer
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)                   # increment the score by 1 for a correct answer
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")
    
    # display the final score
    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
