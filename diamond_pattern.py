n = 10  # Number of rows for the upper triangle

# Upper part of the diamond
for i in range(1, n + 1):  
    # Print spaces for alignment
    for j in range(n - i, 0, -1):  
        print(" ", end="")  
    # Print stars
    for k in range(2 * i - 1):  
        print("*", end="")  
    print()  # Move to the next line

# Lower part of the diamond
for i in range(n - 1, 0, -1):  
    # Print spaces for alignment
    for j in range(n - i):  
        print(" ", end="")  
    # Print stars
    for k in range(2 * i - 1, 0, -1):  
        print("*", end="")  
    print()  # Move to the next line
