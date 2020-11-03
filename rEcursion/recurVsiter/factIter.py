def factorial(n):
    if n < 0:
        print(ValueError("Imputs 0 or greater only"))
    result = 1
    while n != 0:
        result *= n
        n -= 1
    return result

# test cases
print(factorial(3))
print(factorial(0))
print(factorial(5))
print(factorial(-1))