from math import fabs



def approx_equals(number1, number2, epsilon= 10e-4 ):

    return fabs((number1-number2) / number2) < epsilon

