def even_generator():
    num = 2
    while True:
        yield num
        num += 2

# Print first N even numbers
N=int(input("Enter a number:"))
gen=even_generator()

for i in range(N):
    print(next(gen))
