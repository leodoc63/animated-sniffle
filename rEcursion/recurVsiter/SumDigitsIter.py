# Linear O(N), where "N" is the number of digits

def sum_digits(n):
    if n < 0:
        ValueError("Input 0 or greater only!")
    
    result = 0
    while n != 0:
        result += n % 10
        n = n // 10
    return result + n
    
sum_digits(12)
# 1 + 2
sum_digits(552)
# 5 + 5 + 2
print (sum_digits(123456789) == 45)


    