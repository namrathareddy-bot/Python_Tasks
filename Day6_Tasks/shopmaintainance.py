"""

Develop a Python program for a small shop to process customer purchases.
Store product names and prices in a dictionary, items added to the
cart in a list, product categories in a set,and product details using tuples. Create functions to display products, add items to the cart, and

calculate the total bill. Use a recursive function to compute the total price
of all items in the cart. Include exception handling to manage ValueError
(invalid quantity input), ZeroDivisionError (calculation errors),
TypeError (wrong data types in the cart), and NameError (when a product
name entered by the user does not exist).

"""

def total_price(cart):
    # Recursive function to calculate total bill
    if len(cart) == 0:
        return 0
    return cart[0] + total_price(cart[1:])


def shop_system():
    # Dictionary → product : price
    products = {
        "pen": 10,
        "notebook": 50,
        "pencil": 5,
        "eraser": 3
    }

    # Set → categories
    categories = {"stationery"}

    # List → cart items (prices)
    cart = []

    while True:
        try:
            print("\n1. Display Products")
            print("2. Add to Cart")
            print("3. Calculate Total Bill")
            print("4. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                print("\nAvailable Products:")
                for name, price in products.items():
                    # Tuple → (name, price)
                    product_details = (name, price)
                    print(product_details)

            elif choice == 2:
                name = input("Enter product name: ")

                if name not in products:
                    raise NameError

                qty = int(input("Enter quantity: "))

                price = products[name]
                total_item_price = price * qty

                cart.append(total_item_price)

                print(f"{name} added to cart!")

            elif choice == 3:
                if len(cart) == 0:
                    raise ZeroDivisionError

                total = total_price(cart)

                print("Total Bill:", total)

            elif choice == 4:
                break

            else:
                print("Invalid choice")

        except ValueError:
            print("Invalid quantity! Please enter numbers only.")

        except ZeroDivisionError:
            print("Cart is empty! Cannot calculate bill.")

        except TypeError:
            print("Wrong data type in cart!")

        except NameError:
            print("Product not found!")

    print("\nFinal Cart:", cart)


shop_system()
