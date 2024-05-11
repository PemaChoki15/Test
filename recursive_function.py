def reverse_string(s):
    # Base case: if the string is empty or contains only one character
    if len(s) <= 1:
        return s
    else:
        reversed_string = reverse_string(s[1:]) + s[0]
        
        return reversed_string
    
print(reverse_string("hello"))
print(reverse_string("python"))
