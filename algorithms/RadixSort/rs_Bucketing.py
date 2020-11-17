'''
The least significant digit radix sort algorithm
 takes each number in the input list, looks at 
 the digits of that number in order from right 
 to left, and incrementally stuffs each number 
 into the bucket corresponding to the value of 
 that digit.
''' 

def radix_sort(to_be_sorted):
    maximun_value = max(to_be_sorted)
    max_exponent = len(str(maximun_value))

    being_sorted = to_be_sorted[:]
    digits = [[] for digit in range(10)]

    for number in being_sorted:
        number_as_a_string = str(number)
        digit = number_as_a_string[-1]
        digit = int(digit)
        digits[digit].append(number)
    return digits

    
    