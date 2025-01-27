import numpy as np

def function(x):
    # return 2 - x - np.log(3.638 - x)
    return (4 * x**2) - (2 * x) + 1         # Analytical: 0.75 @ 0.25 

# Initial settings
decimalPlaces = 4                       # Number of decimal places to round to for the tolerance
TOLERANCE = 10 ** -(decimalPlaces+1)

bracket = [0, 4]                        # Initial bracket
numIntervals = 10                   

functionEvaluations = 0

while bracket[1] - bracket[0] > TOLERANCE:
    fCurr = function(bracket[0])
    functionEvaluations += 1

    intervalPoints = np.linspace(bracket[0], bracket[1], numIntervals, endpoint=False)
    for i in range(0, len(intervalPoints) - 1):
        fNext = function(intervalPoints[i + 1])
        functionEvaluations += 1

        if fCurr < fNext:
            bracket = [intervalPoints[i - 1], intervalPoints[i + 1]]
            print(f"Bracket: [{bracket[0]:.12f}, {bracket[1]:.12f}]")
            print(f"Function values at bracket: {function(bracket[0]):.6f}, {function(bracket[1]):.6f}")
            break

        fCurr = fNext

print(f"{functionEvaluations} function evaluations for {decimalPlaces} decimal places of tolerance")