import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return 2 - x - np.log(3.638 - x)
    # return (4 * x**2) - (2 * x) + 1         # Analytical: 0.75 @ 0.25 

TOLERANCE = 1e-15

def equalIntervalSearch(func, bracket=[0, 4], numIntervals=10):
    # Initial settings
    functionEvaluations = 0
    iteration = 1

    while abs(bracket[1] - bracket[0]) > TOLERANCE:
        alpha = np.linspace(bracket[0], bracket[1], numIntervals, endpoint=True)
        x = np.linspace(bracket[0], bracket[1], numIntervals, endpoint=True)
        fCurr = func(alpha[0])
        functionEvaluations += 1

        for i in range(0, numIntervals-1):

            fNext = func(alpha[i + 1])
            functionEvaluations += 1

            if fCurr < fNext:
                bracket = [alpha[i - 1], alpha[i + 1]]
                print(f"Bracket after {iteration:02} interval reductions: [{bracket[0]:.16f}, {bracket[1]:.16f}]")
                iteration += 1
                break

            fCurr = fNext
        
    stepSize = (bracket[1] + bracket[0]) / 2

    return stepSize, bracket, functionEvaluations

# Example usage
initialBracket = [0, 4]

intervals = np.linspace(6, 16, 11)
functionEvaluationsT = []

print(f"Initial Bracket: [{initialBracket[0]:.15f}, {initialBracket[1]:.15f}]\n")

for i in range(0, len(intervals)):
    print(f"Number of Intervals: {intervals[i]:.0f}")

    stepSize, bracket, functionEvaluations = equalIntervalSearch(function, bracket=initialBracket, numIntervals=int(intervals[i]))

    print(f"\nTotal Function Evaluations: {functionEvaluations}")
    print(f"Step Size: {stepSize:.15f}")

    functionEvaluationsT.append(functionEvaluations)

plt.plot(intervals, functionEvaluationsT)
plt.xlabel("Number of Intervals")
plt.ylabel("Function Evaluations")
plt.title("Function Evaluations vs. Number of Intervals")
plt.show()
