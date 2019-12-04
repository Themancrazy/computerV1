import re
import sys

def equIsValid(equElems):
    count = 0
    for x in equElems:
        if (x == '='):
            count += 1
    if (count != 1):
        return False
    return True

def reducedForm(equElems):
    realNumb = 0
    UnknownNumb = 0
    QuadUnknownNumb = 0
    if (equIsValid(equElems) == False):
        raise Exception('Invalid equation: equation must countain one \'=\' sign.')
    else:
        if (isQuadraticEquation(equElems)):
            for x in equElems:
                if (isRealNumb(x)):
                    realNumb += getRealNumb(x, equElems)
                if (isUnknownNumb(x))
                    UnknownNumb += getUnknownNumb(x, equElems)
        else if (isEquation(equElems)):

        print("Reduced Form: ", end="")
        print(*equElems)

def dispatchEqu(equation):
    equElems = re.split("[ |\t]+", equation.strip())
    return equElems

def compV1():
    if (len(sys.argv) != 2):
        print("Usage: ./compv1.py <QUAD EQUAT>")
        exit(0);
    try:
        equElems = dispatchEqu(sys.argv[1])
        reducedForm(equElems)
    except Exception as e:
        print("\x1b[91mError: ", str(e), "\x1b[0m")
    # Print Reduced form
    # Print Polynomial degree
    # Print solution:
    #                   - 1st degree: 1 solution
    #                   - 2nd degree: 0, 1 or 2 solutions.
    #                   - 3rd or more degree: return error.

compV1()
