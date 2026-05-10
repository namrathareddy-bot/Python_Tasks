""9. Align text using formatting.
10. Print a table row using formatted strings."""

#9. Align text using formatting
text = "Python"
# Left align
print(f"{text:<10}")
# Right align
print(f"{text:>10}")
# Center align
print(f"{text:^10}")



#10. Print a table row using formatted strings
name = "Sri Lekha"
age = 22
marks = 88.5
print(f"{'Name':<15}{'Age':<10}{'Marks':<10}")
print(f"{name:<15}{age:<10}{marks:<10}")
