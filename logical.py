# Example  1
x = 5
print(x > 3 and x < 10) # True because both conditions are True

# Example 2
y = 12
print(y > 10 and y % 5 == 0) # False because the second conditions is False

# Example 1
x = 5
print(x < 3 or x > 10) # False beacuse both conditions are False

# Example 2
y = 12
print(y < 10 or y % 2 == 0) # True because the second conditions is True

# Example 1
x = 5 
print(not(x > 3 and x < 10)) # False because the condition inside the not is True

# Example 2
y = 12
print(not(y > 10 and y % 5 == 0)) # True because the condiotion inside the not is False