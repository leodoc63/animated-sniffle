# runtime: Linear - O(N)

def factorial(n):
    if n < 0:
        print(ValueError("Imput 0 or greater only"))
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(3))
print(factorial(-1))
