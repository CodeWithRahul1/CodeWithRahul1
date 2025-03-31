def minimumNumber(n, password):
    
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    has_digit = any(char in numbers for char in password)
    has_lower = any(char in lower_case for char in password)
    has_upper = any(char in upper_case for char in password)
    has_special = any(char in special_characters for char in password)

    missing_types = 4 - sum([has_digit, has_lower, has_upper, has_special])
    required_length = max(0, 6 - n)
