def generator(n):
    for i in range(1,n+1):
        yield i
for num in generator(20):
    print(num)
