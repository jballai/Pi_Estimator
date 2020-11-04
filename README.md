# Pi_Estimator

Uses repeated dice rolls to estimate the value of Pi using a Monte-Carlo Simulation.
Takes in as input the number of points you want used in the simulation and outputs an estimate of Pi.

### The Monte-Carlo Simulation to Estimate Pi

https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/

The Monte-Carlo Method uses many randomized values to help predict a specific outcome.  We can use this method to help estimate Pi by incorporating the Unit Circle.
If the Unit Cirlce is inscribed in a square with an area of 1 unit (Both shapes have diameter 1), then we can take the ratio of randomized values inside the circle against the total values in order to get an estimate of Pi.
To get the estimate for Pi, we know the area of the square is 1 unit.  We can figure out the area of the circle because the Area = Pi * (r^2).  So, the Area = Pi * (1/2)^2 = Pi/4.
Therefore, by calculating the ratio above and then multpilying it by 4, we would get an estimate for Pi!

### Base-6
A 'Senary' number, or a number in Base-6, uses numbers 0-5 rather than numbers 0-9 for each digit like we are used to.  So when the decimal number is 6, the base-6 number would
be 10.  

The formula for converting a base-6 number to decimal would be:

0352

0*(6^3) + 3*(6^2) + 5*(6^1) + 2*(6^0) = 0 + 108 + 30 + 2 = 140

### Process
This problem can be broken up into multiple steps:

1)  I take in a 6-sided die roll as an input (Random integer 1-6).  Also, every time I call this function, I call it 4 times.  You will see why in step 2.

2)  In order to set the dice roll inputs up for a Monte-Carlo Simulation, I first take the 4 die rolls and subtract one from each.  Then
    I append them as a sequence of integers in the order that they were rolled.
    For instance, if I roll a 1, 4, 6, 3, the sequence outputted would be a string, '0352'.
    The reason for doing this is now, the outputted string is a 4-bit, base-6 number.
    
3)  I put the dice rolls into base-6 so that we can work with larger numbers of data and generate more precise coordinates later on for the Monte-Carlo Simulation.
    Now that it is a base-6 number, I convert the number into decimal form.  Now the number is a much bigger number that is in the range 0-1295.
    For the example above, the base-6 number '0352', is now 140.
    
4)  In order to get an x and y coordinate for the simulation, the randomized value must be between [0-1].  Something to note here is that I am only using Quadrant I of the    
    graph by only generating values between 0-1 for both x and y.  This does not change the ending answer as long as I am consistent with it.
    
    This is simply done by dividing the newly converted decimal value by 1295, or the maximum value which would make the new max value 1.  In this step, I call the 4 die rolls 
    and the steps that follow for both an x-coordinate and a y-coordinate.
    
5)  Now I have a list of size n (n = user input) of both x-coordinates and y-coordinates.  I run through these lists and check if the distance of the coordinates (x^2 + y^2)
    is less than or equal to 1. If this is the case, then I add that coordinate pair as a point in the circle. 
    
6)   After going through all of the coordinates, I use the equation 4 * (points in the circle / total points) to generate an estimate of pi.
