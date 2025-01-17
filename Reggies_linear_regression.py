# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:03:06 2024

@author: Aidan O'Donoghue
"""

#PROJECT: Reggie's Linear Regression
#------------------------------------------------------------------------------

# Task 1, define straight line function y = m*x+b
def get_y(m, b, x):                             #Define straight line function           
    y = m*x+b                                   #Define line y = mx+b
    return y                                    #Reutn y value for inputted x

# Uncomment each print() statement to check your work. Each of the following 
# should print True
print(get_y(1, 0, 7) == 7)                      #Prints true
print(get_y(5, 10, 3) == 25)                    #Prints true

#------------------------------------------------------------------------------
# Tasks 2 and 3, Write the calculate_error() function here.  Takes the point 
# inputed and calculates the absolute y-error based on y = mx+b
def calculate_error(m, b, point):               #Define error function
    x_point = point[0]                          #Get x-coord from point
    y_point = point[1]                          #Get y-coord from point
    y_from_x_point = get_y(m,b,x_point)         #Get y-coord from y = mx+b
    error = abs(y_point-y_from_x_point)         #Get absolute error between y's
    return error                                #Return the error

#------------------------------------------------------------------------------
# Task 4, Uncomment each print() statement and check the output against the 
# expected result
# this is a line that looks like y = x, so (3, 3) should lie on it. thus, error 
# should be 0:
print(calculate_error(1, 0, (3, 3)))            #Correct
# the point (3, 4) should be 1 unit away from the line y = x:
print(calculate_error(1, 0, (3, 4)))            #Correct
# the point (3, 3) should be 1 unit away from the line y = x - 1:
print(calculate_error(1, -1, (3, 3)))           #Correct
# the point (3, 3) should be 5 units away from the line y = -x + 1:
print(calculate_error(-1, 1, (3, 3)))           #Correct

#------------------------------------------------------------------------------
# Task 5, Write your calculate_all_error() function here.  Takes a bunch of 
# points, calculates the error for each point and adds the errors together
def calculate_all_error(m, b, points):          #Define function to sum all 
                                                #errors for list of points
    error_total = 0;                            #Initial total error
    for item in points:                         #Iterate through all points
        error_total+=calculate_error(m, b, item)#Add error to total error
    return error_total                          #Then return the total error
        
#------------------------------------------------------------------------------
# Task 6, Uncomment each print() statement and check the output against the 
# expected result
# every point in this dataset lies upon y=x, so the total error should be zero:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)] #Given data points      
print(calculate_all_error(1, 0, datapoints))    #Correct     
# every point in this dataset is 1 unit away from y = x + 1, so the total error 
# should be 4:
print(calculate_all_error(1, 1, datapoints))    #Correct
# every point in this dataset is 1 unit away from y = x - 1, so the total error 
# should be 4:
print(calculate_all_error(1, -1, datapoints))   #Correct
# the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, 
# respectively, so total error should be 1 + 5 + 9 + 3 = 18
print(calculate_all_error(-1, 1, datapoints))   #Correct

#------------------------------------------------------------------------------
# Tasks 8 and 9, set up list comprehension with range of possible slopes and
# intercepts
possible_ms = [m*0.1 for m in range(-100,101)]  #Possible slopes in range
possible_bs = [b*0.1 for b in range(-200,201)]  #Possible intercepts in range

#------------------------------------------------------------------------------
# Task 10, set out results of Reggie's tests and define initial smallest error
# and best slope and intercept
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
                                                #Data points from Reggie's tests
smallest_error = float('inf')                   #Initial smallest error
best_m = 0                                      #Initial best slope
best_b = 0                                      #Initial best intercept

#------------------------------------------------------------------------------
# Tasks 11 and 12, calculate the best line slope and intercept for linear 
# regression based by iterating through all m and b combinations and finding 
# smallest error total
for m in possible_ms:                           #Iterate thro' all slopes              
    for b in possible_bs:                       #Iterate thro' all intercepts
        current_error = calculate_all_error(m, b, datapoints)
                                                #Calcuate error at each m and b
        if current_error<=smallest_error:       #If the error is reduced...
            smallest_error = current_error      #...then save it as smallest error 
            best_m = m                          #and save current slope
            best_b = b                          #and current intercept
     
#------------------------------------------------------------------------------
# Task 13, check against the CodeCademy solution.  Its different!  Why!
x1 = 6                                          #Input ball size
y1 = best_m*x1+best_b                           #Output bounce

#------------------------------------------------------------------------------
# Extra task 14, Plot the linear regression line
import matplotlib.pyplot as plt                 #Import plotting library
x = [i for i in range(0,10)]                    #x-values
y = [i for i in range(0,10)]                    #Corresponding y-values
i = 0;                                          #Initialise i
for item in x:                                  #For all x
    y[i] = get_y(best_m, best_b, item)          #Calculate y
    i+=1                                        #Increment i
x2, y2 = zip(*datapoints)                       #Zip points and pivot
plt.plot(x,y)                                   #Plot the line
plt.scatter(x2,y2)                              #Plot the test points
plt.xlabel('x - axis')                          #Label for x-axis
plt.ylabel('y - axis')                          #Label for y-axis
plt.title('Regression Output')                  #Title
plt.grid()                                      #Add a grid

#------------------------------------------------------------------------------
# Extra task 15, so if we are getting different answers to the CodeCademy folks 
# are there more than one solution?  Record all m's and b's that give error = 5
solutions = []                                  #Empty list
for m in possible_ms:                           #Iterate thro' possible slopes
    for b in possible_bs:                       #Iterate thro' possible intercepts
        current_error = calculate_all_error(m, b, datapoints)
                                                #Calculate current error
        if current_error == 5:                  #If this is the smallest error 5
            record_mb = (m,b)                   #Record m and b as a tuple
            solutions.append(record_mb)         #Append tuple to the list
print(list(solutions))                          #Print the possoble solutions

#Guess this was a simplified linear regression.  I think its a bit more complex
#that that!

