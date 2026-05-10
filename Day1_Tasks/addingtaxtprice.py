"""7. Store a price in a variable and add tax to it."""
price = 10000
tax_rate = float(input("enter tax rate in percentage (%): "))
tax_amount = price * tax_rate
total_price = price + tax_amount
print(f"Price:{price: .2f}")
print(f"Tax Rate: {tax_rate*100}%")
print(f"Tax amount: {tax_amount: .2f}")
print(f"Total price after adding tax is:{total_price: .2f}")
