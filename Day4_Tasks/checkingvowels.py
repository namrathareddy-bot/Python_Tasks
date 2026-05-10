"""6. Write a program to count the number of vowels in a string."""
vowels = 'aeiouAEIOU'
st = input("enter string: ")
count_vowels = 0
for char in st:
    if char in vowels:
        count_vowels+=1
print("Number of vowels: ",count_vowels)
