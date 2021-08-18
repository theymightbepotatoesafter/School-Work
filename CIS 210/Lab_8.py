import doctest as dt

def btod(bin_str):
    assert isinstance(bin_str, str)
    print("Your string is " + bin_str)
    return None

#btod("1100101")
#btod(1100101)

def btod(bin_str):
    assert isinstance(bin_str, str)
    for bit in bin_str:
        assert bit in '01', 'A binary number is needed.'
    print("Your string is " + bin_str)
    return None

#btod('1100101')
#btod('123')

def foo(x, y):
    assert isinstance(x, int), "An integer is needed"
    assert isinstance(y, int), "An integer is needed"
    assert y > 0, "Can't divide by zero"

    return x // y

#print(foo(8, 4))
#print(foo(8.0, 4.0))
#print(foo(8,0))

def double_your_num(number):
    assert isinstance(number, int), 'An integer is needed'
    assert (number >= 1) and (number <= 10), 'Number out of bounds'
    print(number * 2)
    return None
    
#double_your_num(3)
#double_your_num(3.5)

def incr_li(li, n):
    '''(list of ints, int) -> None     
    
    Increment the first n values in    
    a list by 1 and print the new list.    
    >>> incr_li([1, 2, 3, 4], 2)    
    [2, 3, 3, 4]     
    >>> incr_li([1, 2, 3, 4], 5)   
    [2, 3, 4, 5]
    '''     
    #newli = li[:] # slicing the entire list creates a copy     
    #for i in range(n): 
    #    newli[i] += 1     
    #print(newli)     
    #return None

    try:
        newli = li[:]
        for i in range(n):
            newli[i] += 1
        print(newli)
    except IndexError:
        newli1 = li[:]
        for i in range(len(newli1)):
            newli1[i] += 1
        print(newli1)

    return None

def catch_zero_divition(x, y):
    '''
    (number, number) -> number

    Divides x by y

    >>> catch_zero_divition(2, 0)
    Denomenator cannot be zero
    >>> catch_zero_divition(2, 4)
    0.5
    '''
    
    try:
        output = x / y
        print(output)
    except ZeroDivisionError:
        print("Denomenator cannot be zero")

print(dt.testmod())