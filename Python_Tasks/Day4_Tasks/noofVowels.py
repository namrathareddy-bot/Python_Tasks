"""9. Write a function that takes a string as input and returns the
number of vowels."""
def vowels():
    st = input("enter string: ")
    vowels = "aeiouAEIOU"
    count = 0
    for ch in st:
        if ch in vowels:
            count += 1
    print(count)
vowels()
