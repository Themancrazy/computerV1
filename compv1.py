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

def isValidExpression(firstExpression):
    if (firstExpression.isdigit() == False):
        if bool(re.match('^[-+x^0123456789]+$', firstExpression)):
            return True
        else:
            return False
    return True

NOTHING_ID = -1
OPERATOR_ID = 0
REAL_ID = 1
X_ID = 2

# def createEquation(equElems, QuadUnknownNumb, UnknownNumb, realNumb):
#     if (isValidExpression(equElems[0]) == False):
#         raise Exception('Invalid equation: Expression is wrong.')
#     # logicPreviousExpression = NOTHING_ID
#     # logicCurrentExpression = REAL_ID + X_ID
#     # logicNextExpression = NOTHING_ID
#     xNeedsToBeReal = 0
#     xNeedsToBeUnknown = 0
#     xNeedsToBeQuadUnknown = 0
#     totRealNumb = 0
#     for x in equElems:
#         if (isRealNumb(x)):
            
#         if (xNeedsToBeReal and bool(re.match('^[0123456789]+$', x) == False):
#             raise Exception('Invalid equation: Expression needs to be a real number and not \"', x, "\".")
#         if (xNeedsToBeUnknown and isUnknownNumb(x) == False):
#             raise Exception('Invalid equation: Expression needs to be a first degree unknown value and not \"', x, "\".")

#         # if (logicCurrentExpression = OPERATOR_ID and x != "+" and x != "-" and x != "*" and x != "/" and x != "="):
#         #     raise Exception('Invalid equation: Expression needs to be an operator and not ', x, ".")
#         # if (logicCurrentExpression = REAL_ID and (bool(re.match('^[-+0123456789]+$', firstExpression)) == False and x != "+" and x != "-"):
#         #     raise Exception('Invalid equation: Expression needs to be a real number and not ', x, ".")
#         # if ((logicCurrentExpression = OPERATOR_ID or logicCurrentExpression = OPERATOR_ID + REAL_ID) and (bool(re.match('^[-+x^0123456789]+$', firstExpression)) == False and x != "+" and x != "-"):
#         #     raise Exception('Invalid equation: Expression needs to be either a real number or an unknown variable and not ', x, ".")
#         # if (logicCurrentExpression = OPERATOR_ID and (x == "+" or x == "-")):
#         #     logicNextExpression = logicPreviousExpression


def isRealNumb(elem):
    if (bool(re.match('^[0123456789]+$', elem) == False)):
        if (elem[0] == '-' or elem[0] == '+'):
            if (bool(re.match('^[0123456789]+$', &elem[1]) == False)):
                raise Exception('Invalid equation: Expression needs to be a real number and not \"', x, "\".")
                return False
    return True

# def isSimpleUnknown(elem):
#     if (bool(re.match('^[x^0123456789]+$', x) == False):
#         if (elem[0] == '-' or elem[0] == '+'):
#             if (bool(re.match('^[x^0123456789]+$', &elem[1]) == False)):
#                 raise Exception('Invalid equation: Expression needs to be a 1st degree unknown value and not \"', x, "\".")
#                 return False
#         else:
#             elem = &elem[1]
    
    


def createEquation(equElems, QuadUnknownNumb, UnknownNumb, realNumb):
    if (isValidExpression(equElems[0]) == False):
        raise Exception('Invalid equation: Expression is wrong.')
    for x in equElems:
        if (isRealNumb(x)):
            print x
            #  do
        # if (isSimpleUnknown(x)):
        
 
def reducedForm(equElems):
    realNumb = 0
    UnknownNumb = 0
    QuadUnknownNumb = 0
    if (equIsValid(equElems) == False):
        raise Exception('Invalid equation: equation must countain one \'=\' sign.')
    else:
        createEquation(equElems, QuadUnknownNumb, UnknownNumb, realNumb)
        print("Reduced Form: ", end="")
        print(*equElems)

def dispatchEqu(equation):
    equElems = re.split("[ |\t]+", equation.strip())
    return equElems

def compV1():
    if (len(sys.argv) != 2):
        print("Usage: ./compv1.py <QUAD EQUAT>")
        exit(0)
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
