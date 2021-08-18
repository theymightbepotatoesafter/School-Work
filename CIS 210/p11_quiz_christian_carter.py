''' 
Prior programming experience quiz.
CIS 210 Project 1-1 Hello-Quiz Solution

Author: Christian Carter

Credits: N/A

Add docstrings to Python functions that implement quiz 1 pseudocode.
(See p11_cricket.py for examples of functions with docstrings.)
'''

def q1(onTime, absent):
    '''
    (bool, bool) -> string
    
    User inputs boolean values and function returns a tailored message
    
    >>>q1(False, False)
    Better late than never.
    >>>q1(True, False)
    Hello!
    '''
    if onTime:
        return('Hello!')
    elif absent:
        return('Is anyone there?')
    else:
        return('Better late than never.')

def q2(age, salary):
    '''
    (int, int) -> bool
    
    User inputs age and salary and function returns bool based on the set values
    
    >>> q2(13, 1000)
    True
    >>> q2(27, 10000)
    False
    >>> q2(27, 10001)
    False
    '''
    return (age < 18) and (salary < 10000)

def q3():
    '''
    (none) -> int
    
    No input and will return a 6
    
    >>> q3()
    6
    
    '''
    p = 1
    q = 2
    result = 4
    if p < q:
        if q > 4:
            result = 5
        else:
            result = 6

    return result

def q4(balance, deposit):
    '''
    (int/float, int/float) -> (int/float)
    
    User inputs balance and deposit and is returned the balance plus ten times the deposit
    
    >>> q4(300, 20)
    500
    >>> q4(300, 20.0)
    500.0
    '''
    count = 0
    while count < 10:
        balance = balance + deposit
        count += 1

    return balance

def q5(nums):
    '''
    docstring -
    (list of numbers) -> int
    
    User inputs list of number and is returned the number of numbers in the list that are greater or equal to 0

    >>> q5([0, 1, 2, 3, 4, 5])    #examples are given
    6
    >>> q5([0, -1, 2, -3, 4, -5])
    3
    '''
    result = 0
    i = 0
    while i < len(nums):
        if nums[i] >= 0:
            result += 1

        i += 1

    return result

def q6():
    '''
    (none) -> int
    
    No user input and won't return anything
    
    >>> q6()
    
    '''
    i = 0
    p = 1
    while i < 4:
        i = 1            #This is making the while loop infinite. If this was removed then the returned value would be 16
        p = p * 2
        i += 1

    return p








    
    
     
        
    
