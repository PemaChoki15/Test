def find_first_repeating_character(s):
    character_count = {}
    
    for character in s:
        # Check if character already encountered
        if character in character_count:
            # Print the memory address of the repeating character
            print(f"The memory address of the first repeating character '{character}' is: {id(character)}")
            return id(character)
        else:
            # Store the count of character
            character_count[character] = 1
    
    # If no repeating character found
    return None

print(find_first_repeating_character("people"))




