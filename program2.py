def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum()) # Keep only alphanumeric characters and convert to lowercase
    return cleaned == cleaned[::-1] #returns true or false for the palindrome check

user_input = input("Enter a string: ") #getting the input string
result = is_palindrome(user_input) #calling the function and storing the result
print(f"{result}")