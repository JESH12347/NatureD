n = 5

# Loop through each row
for i in range(n):
    for j in range(n):
        # Print '*' for the structure of 'A'
        if j == 0 or j == n - 1:  # Left and right sides
            print("*", end="")
        elif i == 0 and j > 0 and j < n - 1:  # Top horizontal line
            print("*", end="")
        elif i == n // 2 and j > 0 and j < n - 1:  # Middle horizontal line
            print("*", end="")
        elif i > 0 and i < n // 2 and (j == i or j == n - 1 - i):  # Diagonals
            print("*", end="")
        else:
            print(" ", end="")  # Print space for empty parts
    print() 