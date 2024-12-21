# Function to print a mirrored right triangle pattern
def mirror_right_triangle(rows):
    for i in range(1, rows + 1):
        # Print spaces
        for j in range(rows - i):
            print(" ", end=" ")
        # Print stars
        for k in range(i):
            print("*", end=" ")
        # Move to the next line
        print()

# Number of rows for the triangle
rows = 5
mirror_right_triangle(rows)
