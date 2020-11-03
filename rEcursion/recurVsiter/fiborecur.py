# runtime: Exponential - O(2^N)

def fibonacci(n):
    if n < 0:
        ValueError("Imput 0 or greater only!")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(3))
print(fibonacci(7))
print(fibonacci(1))


