import re
import sys
import fileinput
import matplotlib.pyplot as plt
import numpy as np
# -------------------------------------------------------
# Functions to check if elements of equation are valid.
# -------------------------------------------------------
def isRealNumb(elem):
    if (bool(re.match('^[0123456789]+$', elem)) or ((elem[0] == '-' or elem[0] == '+') and bool(re.match('^[0123456789]+$', elem[1:])))):
        return True
    return False

def isUnknown(elem, pow):
    if (elem.find('X') != -1 and bool(re.match('^[X^0123456789]+$', elem))):
        if (elem.count("X^" + str(pow)) != 1):
            return False
        else:
            return True
    return False

def isOperand(elem):
    if (elem == "+" or elem == "-" or elem == "*" or elem == "/" or elem == "="):
        return True
    return False

# -------------------------------------------------------
# Some usefull math functions.
# -------------------------------------------------------

def absoluteValue(x):
    if (x < 0):
        x *= -1
    return x

def squareRoot(x, PRECISION=0.000001):
    y=1.0
    while (absoluteValue(x / y - y) > PRECISION):
        y = (y + x / y) / 2.0
    return y

# -------------------------------------------------------
# Draw graph.
# -------------------------------------------------------

def drawGraph(a, b, c):
    if (a != 0):
        x = np.linspace(-3,3,11)
        y = a * x**2 + b * x + c
        plt.plot(x,y)
        plt.title("Parabola curve")
        plt.xlabel("x axis")
        plt.ylabel("y axis")
        plt.grid()
        plt.show()
    elif (b != 0):
        x = np.linspace(-3,3,11)
        y = b * x + c
        plt.plot(x,y)
        plt.title("Line")
        plt.xlabel("x axis")
        plt.ylabel("y axis")
        plt.grid()
        plt.show()


# -------------------------------------------------------
# Determine and print solutions.
# -------------------------------------------------------

def simpleEquationSol(a, b):
    sol = -b / a
    print("\x1b[1mThe solution is:\x1b[0m")
    print("\x1b[92m" + str(sol), "\x1b[0m")    
    if (len(sys.argv) == 3 and sys.argv[2] == "-g"):
        drawGraph(0, a, b)

import math

def quadEquationSols(a, b, c):
    discriminant = (b * b) - 4 * a * c

    if (discriminant < 0):
        print("\x1b[1mDiscriminant is \x1b[0m\x1b[91mnegative\x1b[0m\x1b[1m, there's no real solution (real number).\x1b[0m")
    elif (discriminant > 0):
        sol1 = (-b + squareRoot((b * b) - 4 * a * c)) / (2 * a)
        sol2 = (-b - squareRoot((b * b) - 4 * a * c)) / (2 * a)
        print("\x1b[1mDiscriminant is strictly \x1b[0m\x1b[92mpositive\x1b[0m\x1b[1m, the two solutions are:\x1b[92m")
        print('%.2f'%sol1)
        print('%.2f'%sol2)
        print("\x1b[0m", end="")
        if (len(sys.argv) == 3 and sys.argv[2] == "-g"):
            drawGraph(a, b, c)
    elif (discriminant == 0):
        sol1 = (-b + squareRoot((b * b) - 4 * a *c)) / 2 * a
        print("\x1b[1mDiscriminant is \x1b[91mnull\x1b[0m, the only solution is:\x1b[96m")
        print('%.2f'%sol1)
        print("\x1b[0m", end="")
        if (len(sys.argv) == 3 and sys.argv[2] == "-g"):
            drawGraph(a, b, c)

def calculateSols(a, b, c, degree):
    if (degree == "\x1b[92m0\x1b[0m" and c == 0):
        print("\x1b[1m\x1b[91mInfinte\x1b[0m\x1b[1m amount of solutions (all reals are a solution).\x1b[0m")
    if (degree == "\x1b[92m0\x1b[0m" and c != 0):
        print("\x1b[1m\x1b[91mNo\x1b[0m\x1b[1m solutions exist.\x1b[0m")
    elif (degree == "\x1b[93m1\x1b[0m"):
        simpleEquationSol(b, c)
    elif (degree == "\x1b[91m2\x1b[0m"):
        quadEquationSols(a, b, c)


# -------------------------------------------------------
# Determine reduced form of equation and polynomial degree.
# -------------------------------------------------------

def printReducedForm(a, b, c):
    print("\x1b[4m\x1b[1mReduced form:\x1b[0m ", end="")
    aActive = False
    bActive = False
    cActive = False
    if (a != 0):
        print("\x1b[91m" + str(a) + " * X^2 \x1b[0m", end="")
        aActive = True
    if (b != 0):
        bActive = True
        if (b >= 0):
            if (aActive):
                print("+ ", end="")
            print("\x1b[93m" + str(b) + " * X^1 \x1b[0m", end="")
        if (b < 0):
            if (aActive):
                print("- ", end="")
            print("\x1b[93m" + str(-b) + " * X^1 \x1b[0m", end="")
    if (c != 0):
        cActive = True
        if (c >= 0):
            if (bActive or aActive):
                print("+ ", end="")
            print("\x1b[92m" + str(c) + "\x1b[0m", end="")
        if (c < 0):
            if (bActive or aActive):
                print("- ", end="")
            print("\x1b[92m" + str(-c) + "\x1b[0m", end="")
    if (aActive == False and bActive == False and cActive == False):
        print("0", end="")
    print(" = 0")
    polDeg = "\x1b[92m0\x1b[0m"
    if (a != 0):
        polDeg = "\x1b[91m2\x1b[0m"
    elif (b != 0):
        polDeg = "\x1b[93m1\x1b[0m"
    # elif (c != 0):
        # polDeg = "0"
    print("\x1b[4m\x1b[1mPolynomial degree:\x1b[0m " + polDeg + "\x1b[0m")
    return polDeg

def reducedForm(equElems):
    a = 0
    b = 0
    c = 0
    i = 0
    equal = -1
    while (i < len(equElems)):
        if (isRealNumb(equElems[i]) == False and isUnknown(equElems[i], 0) == False and isUnknown(equElems[i], 1) == False and isUnknown(equElems[i], 2) == False and isOperand(equElems[i]) == False):
            raise Exception("Invalid element: " + equElems[i])
        if (isRealNumb(equElems[i]) and equal == -1):
            if (isUnknown(equElems[i + 2], 0)):
                if (i > 0 and equElems[i - 1] == "-"):
                    c -= float(equElems[i])
                elif (i > 0 and equElems[i - 1] == "+"):
                    c += float(equElems[i])
                elif (i <= 0):
                    c += float(equElems[i])
                else:
                    raise Exception("Invalid operand: " + equElems[i - 1])
            elif (isUnknown(equElems[i + 2], 1)):
                if (i > 0 and equElems[i - 1] == "-"):
                    b -= float(equElems[i])
                elif (i > 0 and equElems[i - 1] == "+"):
                    b += float(equElems[i])
                elif (i <= 0):
                    b += float(equElems[i])
                else:
                    raise Exception("Invalid operand: " + equElems[i - 1])
            elif (isUnknown(equElems[i + 2], 2)):
                if (i > 0 and equElems[i - 1] == "-"):
                    a -= float(equElems[i])
                elif (i > 0 and equElems[i - 1] == "+"):
                    a += float(equElems[i])
                elif (i <= 0):
                    a += float(equElems[i])
                else:
                    raise Exception("Invalid operand: " + equElems[i - 1])
        elif (equElems[i] == "=" or equal == 1):
            equal = 1
            if (isRealNumb(equElems[i]) and int(equElems[i]) != 0):
                if (isUnknown(equElems[i + 2], 0)):
                    if (i > 0 and equElems[i - 1] == "-"):
                        c += float(equElems[i])
                    elif (i > 0 and equElems[i - 1] == "+" or equElems[i - 1] == "="):
                        c -= float(equElems[i])
                    else:
                        raise Exception("Invalid operand: " + equElems[i - 1])
                elif (isUnknown(equElems[i + 2], 1)):
                    if (i > 0 and equElems[i - 1] == "-"):
                        b += float(equElems[i])
                    elif (i > 0 and equElems[i - 1] == "+" or equElems[i - 1] == "="):
                        b -= float(equElems[i])
                    else:
                        raise Exception("Invalid operand: " + equElems[i - 1])
                elif (isUnknown(equElems[i + 2], 2)):
                    if (i > 0 and equElems[i - 1] == "-"):
                        a += float(equElems[i])
                    elif (i > 0 and equElems[i - 1] == "+" or equElems[i - 1] == "="):
                        a -= float(equElems[i])
                    else:
                        raise Exception("Invalid operand: " + equElems[i - 1])
        i += 1
    polDeg = printReducedForm(a, b, c)
    calculateSols(a, b, c, polDeg)

# -------------------------------------------------------
# Parser functions.
# -------------------------------------------------------

def dispatchEqu(equation):
    equElems = re.split("[ |\t]+", equation.strip())
    for x in equElems:
        x = x.strip()
    if (equElems.count("=") > 1):
        raise Exception("Equation can't countain more than 1 equal sign ('=').")
    if (isRealNumb(equElems[0]) == False and isUnknown(equElems[0], 0) == False and isUnknown(equElems[0], 1) == False and isUnknown(equElems[0], 2) == False):
        raise Exception(equElems[0] +" is invalid. Equation has to start with a real or x.")
    return equElems

def readStdin():
    for line in fileinput.input():
        return (line.rstrip())
    return "ERROR"

def compV1():
    equation = "ERROR"
    if ((len(sys.argv) > 3) or (len(sys.argv) == 3 and sys.argv[2] != "-g")):
        print("Usage: ./compv1.py <QUAD EQUAT> (-g)")
        exit(0)
    elif (len(sys.argv) == 1):
        equation = readStdin()
    else:
        equation = sys.argv[1]
    try:
        equElems = dispatchEqu(equation)
        reducedForm(equElems)
    except Exception as e:
        print("\x1b[91mError: ", str(e), "\x1b[0m")

compV1()
