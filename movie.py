age = int(input("Enter your age: "))

# Ask the user to enter whether they are student or not
student = input("Are you student? (yes/no): ")

# Use the logical operators to determine if the person is eligible
eligible_for_discount = (age <= 12) or (13 <= age <= 18 and student == 'yes')

# Print the results
if eligible_for_discount:
    print("You are eligible for a discount on the movie ticket.")
else:
    print("YOu are not eligible for a discount on the movie ticket.")
    