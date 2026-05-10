class Result:
    def calculate(self,n1,n2,n3=None):
        if m3 is None:
            total=n1+n2
        else:
            total=n1+n2+n3
        print("Total Marks:",total)
r=Result()
r.calculate(30,40)
r.calculate(30,40,70)
