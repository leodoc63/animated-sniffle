'''
For every iteration, radix sort renders a 
version of the input list that is sorted based
 on the digit that was just looked at. At first 
 pass, only the ones digit is sorted. At the 
 second pass, the tens and the ones are sorted. 
 This goes on until the digits in the largest 
 position of the largest number in the list are 
 all sorted, and the list is sorted at that time.

'''

def radix_sort(to_be_sorted):
    maximun_value = max(to_be_sorted)
    max_exponent = len(str(maximun_value))
    being_sorted = to_be_sorted[:]
    
    #Add new for-loop here:
    for exponent in range(max_exponent):
        position = exponent + 1
        index = -position
        digits = [[] for digit in range(10)]

    for number in being_sorted:
        number_as_a_string = str(number)
        digit = number_as_a_string[index]
        digit = int(digit)
        digits[digit].append(number)
    
    # reassign bein_sorted here:
    # .extend() appends all the elements of a
    #list, instead of appending the list itself
    being_sorted = []
    for numeral in digits:
        being_sorted.extend(numeral)
    return being_sorted
