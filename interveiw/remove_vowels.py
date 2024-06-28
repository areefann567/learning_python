def remove_vowels(input_str):
    vowels = "AEIOUaeiou" 
    filtered_str = ""
    for char in input_str:
        if char not in vowels:
            filtered_str += char
    return filtered_str


input_str = "Hello, World!"
result = remove_vowels(input_str)
print("Original string:", input_str)
print("String without vowels:", result)
