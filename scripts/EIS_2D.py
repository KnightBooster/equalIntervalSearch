from math import sqrt
import numpy as np
from scipy.optimize import minimize

# TODO: Implements the function to check if the given search direction is a descent direction
def isDescentDirection(function: callable, searchDirection, initialX):
    h = 1e-5
    grad_f = np.zeros(len(initialX))
    for i in range(len(initialX)):
        x = initialX.copy()
        x[i] += h
        grad_f[i] = (function(x) - function(initialX)) / h

    return np.dot(grad_f, searchDirection) < 0

def equalIntervalSearch(objectiveFunction: callable, initialX: list, searchDirection: list, bracket: list, numIntervals: int, printBracket: bool = True) -> tuple:
    bracketReduction = 0
    functionEvaluations = 0
    TOLERANCE = 1e-15

    if not isDescentDirection(objectiveFunction, searchDirection, initialX):
        raise ValueError("The search direction is not a descent direction")
    
    while abs(bracket[1] - bracket[0]) > TOLERANCE:
        alpha = np.linspace(bracket[0], bracket[1], numIntervals, endpoint=True)

        x1 = initialX[0] + (alpha[0] * searchDirection[0])
        x2 = initialX[1] + (alpha[0] * searchDirection[1])
        fCurr = objectiveFunction([x1, x2])

        functionEvaluations += 1

        for i in range(0, numIntervals-1):
            x1 = initialX[0] + (alpha[i + 1] * searchDirection[0])
            x2 = initialX[1] + (alpha[i + 1] * searchDirection[1])

            fNext = objectiveFunction([x1, x2])
            functionEvaluations += 1

            if fCurr < fNext:
                bracket = [alpha[i - 1], alpha[i + 1]]
                bracketReduction += 1

                if printBracket:
                    print(f"Bracket after {bracketReduction:02} interval reductions: [{bracket[0]:.16f}, {bracket[1]:.16f}]")
                break

            fCurr = fNext

    stepSize = (bracket[1] + bracket[0]) / 2

    return stepSize, bracketReduction, functionEvaluations

def verifyMinima(objectiveFunction: callable, initialX: list, searchDirection: list):
    def lineSearchFunction(alpha):
        x = [initialX[0] + alpha * searchDirection[0], initialX[1] + alpha * searchDirection[1]]
        return objectiveFunction(x)

    result = minimize(lineSearchFunction, 0)
    alpha_opt = result.x[0]
    x_opt = [initialX[0] + alpha_opt * searchDirection[0], initialX[1] + alpha_opt * searchDirection[1]]
    return x_opt

if __name__ == "__main__":

# !To be provided by the user
    def function(x):
        x1 = x[0]
        x2 = x[1]
        return (10 * x1**2) + (4 * x2**2) + (3 * x1 * x2) + (2 * x1) + (2 * x2) + 1

    initialX = [1, 1]
    searchDirection = [-7/sqrt(53), -2/sqrt(53)]
    bracket = [0, 10]
    numIntervals = 10

    stepSize, bracketReduction, functionEvaluations = equalIntervalSearch(function, initialX, searchDirection, bracket, numIntervals, printBracket=False)
    x1, x2 = initialX[0] + (stepSize * searchDirection[0]), initialX[1] + (stepSize * searchDirection[1])
    
    print(f"Bracket Reductions: {bracketReduction}")
    print(f"Function Evaluations: {functionEvaluations}")

    print(f"Step Size: {stepSize:.16f}")
    print(f"Minima: {function([x1, x2]):.16f} using Equal Interval Search")
    print(f"Minima at [{x1:.16f}, {x2:.16f}] using Equal Interval Search")

    x_opt = verifyMinima(function, initialX, searchDirection)
    print(f"Minima at [{x_opt[0]:.16f}, {x_opt[1]:.16f}] using Scipy's minimize function (scipy.optimize.minimize)")