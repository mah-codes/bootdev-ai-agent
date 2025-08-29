#!/usr/bin/env python3
"""
Examples of how to use the ** (dictionary unpacking) operator in Python
"""

# Example 1: Using ** to pass dictionary as keyword arguments to a function
def greet(name, age, city):
    return f"Hello {name}, you are {age} years old and live in {city}"

person_info = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# This unpacks the dictionary as keyword arguments
result = greet(**person_info)
print("Example 1 - Function call with **:")
print(result)
print()

# Example 2: Using ** to merge dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5}

# Merge multiple dictionaries
merged = {**dict1, **dict2, **dict3}
print("Example 2 - Dictionary merging with **:")
print(f"dict1: {dict1}")
print(f"dict2: {dict2}")
print(f"dict3: {dict3}")
print(f"merged: {merged}")
print()

# Example 3: Using ** in function definitions to accept arbitrary keyword arguments
def flexible_function(required_arg, **kwargs):
    print(f"Required argument: {required_arg}")
    print("Additional keyword arguments:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("Example 3 - Function definition with **kwargs:")
flexible_function("hello", name="Bob", age=25, hobby="reading")
print()

# Example 4: What happens if you try to use ** alone (your original attempt)
some_dict = {'title': 'Paris Memoirs', 'author': 'Austin Powers'}
print("Example 4 - Why **some_dict alone doesn't work:")
print("This would cause a SyntaxError:")
print("**some_dict  # <- This is invalid syntax")
print()
print("But you can use it in these contexts:")
print(f"In a new dict: {{'new_key': 'new_value', **some_dict}}")
print()

# Example 5: Real-world use case - building API requests
def make_api_request(endpoint, method='GET', **params):
    print(f"Making {method} request to {endpoint}")
    if params:
        print(f"With parameters: {params}")

api_params = {'user_id': 123, 'limit': 10, 'sort': 'date'}
print("Example 5 - API request with parameters:")
make_api_request('/api/users', method='POST', **api_params)
