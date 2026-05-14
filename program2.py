def is_palindrome(s):
    # Keep only alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    return cleaned == cleaned[::-1]

user_input = input("Enter a string: ")
result = is_palindrome(user_input)
print(f"{result}")