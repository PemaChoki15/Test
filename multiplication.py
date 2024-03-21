try:
    number = int(input("Enter the number for which you want the multiplication table: "))
    limit = int(input("Enter the limit up to which you want the multiplication table generated: "))
    
    if number <= 0 or limit <= 0:
        print("Please enter positive numbers.")
    else:
        print(f"Multiplication Table for {number} up to {limit}:")
        for i in range(1, limit + 1):
            print(f"{number} x {i} = {number * i}")
except ValueError:
    print("Invalid input. Please enter integers only.")
