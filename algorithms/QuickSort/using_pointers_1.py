my_list = ['pizza', 'burrito', 'sandwich', 'salad', 'noodles']

start_of_list = 0
end_of_list = len(my_list) - 1

final_list = my_list[start_of_list : end_of_list + 1]

print(final_list)

end_of_half_sub_list = len(my_list) // 2

right_list = my_list[start_of_list : end_of_half_sub_list + 1]

print(right_list)

start_of_sub_list = 1

end_of_sub_list = len(my_list) - 1

list_without_ends = my_list[start_of_sub_list : end_of_sub_list]

print(list_without_ends)



