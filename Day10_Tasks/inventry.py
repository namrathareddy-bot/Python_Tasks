import numpy as np
inventory_data = np.array([[10,15],[20,25]])
print("The inventory stock data is: ",inventory_data)
new_shipment_data = inventory_data + 2
print(f"The new shipment data after increasing quantity is : {new_shipment_data}")
