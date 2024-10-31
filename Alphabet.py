

result_str = ""
for row in range(0, 7):
    # Iterate through columns from 0 to 6 using the range function
    for column in range(0, 7):
        # Check conditions to determine whether to place '*' or ' ' in the result string
        
        # If conditions are met, place '*' in specific positions based on row and column values
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
            result_str = result_str + "*"  # Append '*' to the 'result_str'
        else:
            result_str = result_str + " "  # Append space (' ') to the 'result_str'

    result_str = result_str + "\n"  

print(result_str) 