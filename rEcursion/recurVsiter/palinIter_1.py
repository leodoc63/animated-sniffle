def is_palindrome(my_string):
    string_lenght = len(my_string)
    middle_index = string_lenght // 2
    for index in range(0, middle_index):
        opposite_character_index = string_lenght - index - 1
        if my_string[index] != my_string[opposite_character_index]:
            return False
    return True
        
print(is_palindrome("abba") == True)
print(is_palindrome("abcba") == True)
print(is_palindrome("") == True)
print(is_palindrome("abcd") == False)