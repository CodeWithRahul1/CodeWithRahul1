def roman_to_int(s):
    # Define Roman values
    symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    values  = [1,   5,  10, 50, 100, 500, 1000]
    
    def value_of(ch):
        for i in range(len(symbols)):
            if symbols[i] == ch:
                return values[i]
        return 0  # fallback

    total = 0
    i = 0

    while i < len(s):
        # Get value of current symbol
        current = value_of(s[i])

        # Look ahead to next symbol if any
        if i + 1 < len(s):
            next_val = value_of(s[i + 1])
            if current < next_val:
                # Subtraction case (e.g., IV, IX)
                total += next_val - current
                i += 2  # Skip next symbol
            else:
                total += current
                i += 1
        else:
            total += current
            i += 1

    return total

# Examples
print(roman_to_int("III"))      # Output: 3
# print(roman_to_int("LVIII"))    # Output: 58
# print(roman_to_int("MCMXCIV"))  # Output: 1994
