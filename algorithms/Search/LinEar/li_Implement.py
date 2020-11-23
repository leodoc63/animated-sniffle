'''
# For each element in the search_list
    # if element equal target value then
       # return its index
# if element is not found then 
    # raise a ValueError
'''

# define your linear search below
def linear_search(search_list, target_value):
    for idx in range(len(search_list)):
        print (search_list[idx])
        if search_list[idx] == target_value:
            return idx
    raise ValueError("{0} not in list".format(target_value))


# uncomment the lines below to test ...

values = [54, 22, 46, 99]

print(linear_search(values, 30))