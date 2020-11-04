'''
Created on Oct 12, 2020

@author: Joseph Ballai

Question 2: Pi.py
'''
import random

def rollDice():
    '''Note: I am using the range of (0, 5) rather than a normal dice roll which would be (1, 6).  It is easier to work with when I am 
    converting from base 6 to decimal.  This can be seen as whatever number the die lands on minus 1 or if the die lands on a 6, we 
    count it as 0. '''
    return random.randint(1, 6)

def base_six_to_decimal():
    '''
    In order to create a completely random number that does not only list an option of 6 different integers, I am taking a sequence 
    of 4 die rolls and in order, converting that sequence as a number of base 6 to a decimal.  For instance, if I roll a 0, 3, 5, and then 2, the 
    created sequence is 0352.  Then, 0352 converted from base 6 to a decimal is 140. 
    Note: In order to place the randomly generated coordinate on the unit circle later on, I will divide the created decimal (140 in my
    example) by 1295 because that is the highest possible number that can be created by a 4-digit base 6 number and the highest number
    I want for my upper bound is 1.  
    Note 2: To be able to imagine this, I will only be using the top right portion of the Unit Circle (Quadrant 1) so that I can work 
    with only positive numbers. 
    '''
    base_6 = str(rollDice()-1) + str(rollDice()-1) + str(rollDice()-1) + str(rollDice()-1) 
    if base_6 == '0000':
        return 0
    decimal = int(base_6[0])
    for i in base_6[1:]:
        decimal *= 6
        decimal += int(i)
    return decimal


def pi_estimator(n):
    count = 0
    x_lst = []
    y_lst = []
    distance = []
    square_point = 0
    circle_point = 0
    #Creates a list of size n of randomized die rolls for an x coordinate and a y coordinate
    while count < n:
        x_lst.append(float(base_six_to_decimal() / 1295))
        y_lst.append(float(base_six_to_decimal() / 1295))
        #By dividing by 1295 the values in these lists are now bound between 0 and 1 since 1295 is the maximum value of a 4 digit 
        #base-6 number.  Since they are bound between 0 and 1, we are only using Quadrant 1, which is all positive numbers.
        count += 1
        
    #This portion calculates the distance of the coordinate in relation to the unit circle.  
    #If the distance is greater than 1, it would be outside of the circle and it will always be inside the square.
    for i in range(len(x_lst)):
        distance.append(x_lst[i]**2 + y_lst[i]**2)
        if distance[i] <= 1:
            circle_point += 1
        square_point += 1
    #Given formula in order to solve for pi
    pi = 4*(circle_point / square_point)
    return pi

print(pi_estimator(1000))
