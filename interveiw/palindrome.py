def is_palindrome(name):
    reverse=name[::-1]
    return  name==reverse

word="mad"
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")




    