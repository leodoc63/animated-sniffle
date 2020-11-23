'''
In the text editor, you will find the code for 
the linear_search() function that we implemented
 in Python.

When called, our function returns either an index
 of an element that matches the target value or a
 ValueError express that the value was not found.

The text editor includes the code for the 
linear_search() function, a list of numbers 
called number_list and a variable called 
target_number, which stores target value 
that we will be searching for in number_list. 
'''

number_list = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
target_number = 100

def linear_search(search_list, target_value):
    for idx in range(len(search_list)):
        print(search_list[idx])
        if search_list[idx] == target_value:
            return idx
    raise ValueError("{0} Not in list".format(target_value))
    

try:
    result = linear_search(number_list, target_number)
    print(result)
    
except ValueError as error_message:
    print("{0}".format(error_message))
    
        