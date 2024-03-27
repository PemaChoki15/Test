def reverse_string(s):
    # Base case: if the string is empty or contains only one character
    if len(s) <= 1:
        return s
    else:
        # Recursive case: separate the first character and the rest of the string
        first_char = s[0]
        remaining_chars = s[1:]
        
        # Recursively call reverse_string on the remaining characters
        reversed_remaining_chars = reverse_string(remaining_chars)
        
        # Append the first character to the end of the reversed string
        reversed_string = reversed_remaining_chars + first_char
        
        return reversed_string

# Test cases
print(reverse_string("hello"))  # Output: "olleh"
print(reverse_string("python"))  # Output: "nohtyp"
print(reverse_string(""))        # Output: ""
