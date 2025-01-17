def fibonacci(n):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    # List to store the Fibonacci sequence
    result = []
    
    # Generate the first n Fibonacci numbers
    for _ in range(n):
        # Append the current Fibonacci number to the result list
        result.append(a)
        
        # Update the next Fibonacci numbers
        a, b = b, a + b  # Move to the next two numbers in the sequence

    return result

# Example usage
print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]