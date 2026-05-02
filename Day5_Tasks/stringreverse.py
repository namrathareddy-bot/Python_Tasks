"""4. Write a recursive function to reverse a string."""
def string_reverse(s):
    if len(s) == 0:
        return s
    return string_reverse(s[1:]) + s[0]

st = input("Enter string: ")
print(string_reverse(st))
