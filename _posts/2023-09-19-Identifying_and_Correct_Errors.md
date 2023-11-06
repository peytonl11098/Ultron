---
toc: true
comments: false
layout: post
title: Identifying and Correct Errors
description: Team Test Section 4
type: hacks
courses: { compsci: {week: 5} }
---

## First, we define our function.
This function takes two numbers and divides them.<br>
Here, we also test using non-zero numbers to see if the function works for regular division
# Function to divide two numbers that are inputted.
def divide(a,b):
    # Raise a Value Error if there is division by 0
    if b == 0:
        raise ValueError("Divison by 0 is undefined")
    # Otherwise, return the result
    else:
        output = a / b
    return output
# First we test division with two numbers that can be divided to ensure that the function works for regular division
result = divide(6,3)
assert result == 2, "Expected result for 6 / 3 is 2, but got {}".format(result)
print(f"Test passed: divide(6, 3) correctly returned 2")
## Now we can test, using a try/catch statement first.
Here we force the function to do division by 0 using a try statement.<br>
If there is a Value Error, we know that the function worked properly.
# Here we test to see if the function works when encountering division by 0 using try/catch statements
try:
    result = divide(8, 0)
    print("Test failed: Expected ValueError, but got result:", result)
except ValueError as e:
    print("Test passed:", str(e))
## Now we test using a if/else statement.
Here we force the function to do division by 0 using a if statement.<br>
If an output is returned from the function, the function has failed, but if there is no output then the function passed.
# Here we test to see if the function works when encountering division by 0 using if/else statements
result = None
if 0!=0:
    result = divide(8, 0)
if result is not None:
    print("Test failed: Expected ValueError, but got result:", result)
else:
    print("Test passed: divide(8, 0) correctly handled division by zero.")