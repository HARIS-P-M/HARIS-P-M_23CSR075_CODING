def is_palindrome(s):
    # Keep only alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]


user_input = input("Enter a string: ")
result = is_palindrome(user_input)
status = "True" if result else "False"
print(f"{result}")