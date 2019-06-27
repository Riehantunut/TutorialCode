# 'dataset' holds the input data for this script

import pandas as pd
import numpy as np

ArrayOfClosingPrices = dataset.loc[:,"Close"].values
TiltArray = np.zeros(len(ArrayOfClosingPrices))

#-------------------------------------------------------------------------------------------------------------------------------------------
def leastSquaresMethod(array):
    # Uses least squares method to compute the mean tilt of the array assuming that it follows a straight curve (y=kx+m).
    # It calculates the tilt by k = ( sum(x*y)-sum(x)*sum(y)/n ) / ( sum(x^2)- sum(x)^2/n ), where n is len(array), x is the price, y is the position of the data.
    # The function returns the tilt.

    n = len(array)
    sumY = 0
    for i in range(1, len(array) + 1):
        sumY += i

    sumX = sum(array)

    sumX2 = 0
    for i in array:
        sumX2 += i*i

    sumXY = 0
    counter = 1
    for i in array:
        sumXY += counter * i
        counter += 1

    upperside = sumXY - (sumX * sumY)/n  # The equation is divided into the upperside and underside of the division to make it easier to understand.
    downside = sumX2 - (sumX*sumX)/n

    if(downside == 0):        # To skip division by zero, which happens when python approximates a very small number with zero.
        downside = 0.0000001  # Unfortunately this means that this algorithm will not be exact for large (1000+) arrays :(

    return upperside/downside
#---------------------------------------------------------------------------------------------------------------------------------------

tiltOfPoint = 0

for i in range(len(ArrayOfClosingPrices)):
    if(i <=5):
        pass
    else:
        tiltOfPoint = leastSquaresMethod(ArrayOfClosingPrices[i-5:i])
    TiltArray[i] = tiltOfPoint

dataset["Historical tilt"] = TiltArray
