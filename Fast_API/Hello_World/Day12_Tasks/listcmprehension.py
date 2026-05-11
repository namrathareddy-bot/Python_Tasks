prices=[100,200,300,400]
discount=[p*0.9 if p>200 else p for p in prices]
print("after discount",discount)      
