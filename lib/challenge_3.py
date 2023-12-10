def consonant_value(word):
    vowels = 'aeiou'
    max_consonant_value = 0
    current_consonant_value = 0

    for char in word:
        if char.isalpha() and char not in vowels:
            current_consonant_value += ord(char) - ord('a') + 1
        else:
            if current_consonant_value > max_consonant_value:
                max_consonant_value = current_consonant_value
            current_consonant_value = 0

    return max(max_consonant_value, current_consonant_value)
