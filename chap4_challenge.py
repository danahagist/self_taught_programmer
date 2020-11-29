# Chapter 4 challenges

# 1. Write a function that takes a number as an input and returns that number squared.

def squared(x):
    '''
    function squares your input
    :param x: int.
    : return: squared x.
    '''
    return x**2

print('Below result should be 4')
print(squared(2))

# 2. Create a function that acepts a string as a parameter and prints it.
def print_string(my_string):
    '''
    prints the input string
    :param my_string: str
    : print: prints the string
    '''
    print(my_string)

print('below result should read, well hello there bro!')
print_string('well hello there bro!')


#3. Write a function that takes three required parameters and two optional paramters

def diff_inputs(a,b,c,d=4,e=5):
    '''
    returns the sum of all inputs
    :param a: int.
    :param b: int
    :param c: int.
    :param d: optional int.
    :param e: optional int.
    '''
    return a+b+c+d+e

print('below should return 5')
print(diff_inputs(1,1,1,1,1))


# 4. Write a program with two functions.
# The first function should take an integer as a parameterand return the result of the integer divided by 2.
# The second function should take an integer as a parameter and return the result of the integer multipled by 4.
# Call the first function save the result as a variable,
# and pass it as a parameter to the second function

def div_func(x):
    '''
    returns x/2
    :param x: int.
    return: x divided by 2
    '''
    return x/2

def mult_func(y):
    '''
    returns y * 4
    :param y: int.
    :return: float result of y times 4
    '''
    return y * 4

print('below result should return 20')
div_result = div_func(10)
mult_result = mult_func(div_result)
print(mult_result)



# 5. Write a function that converts a string to a float and returns a result.
# Use exception handling to catch the exception that could occur.

def float_conv(x):
    '''
    converts x to float
    :param x: string form of float.
    :return: string converted to float
    '''
    try:
        return float(x)
    except ValueError:
        print('you gotta give me something convertible, fool!')

print('below result should return 18.6')
print(float_conv('18.6'))

# 6. Add a docstring to all of the functions you wrote in challenges 1-5.
