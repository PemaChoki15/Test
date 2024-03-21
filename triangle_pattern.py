try:
    height = int(input("Enter the height of the triangle (number of rows): "))
    
    if height <= 0:
        print("Please enter a positive integer.")
    else:
        print("Right Triangle Pattern:")
        for i in range(1, height + 1):
            print("*" * i)
except ValueError:
    print("Invalid input. Please enter an integer.")
