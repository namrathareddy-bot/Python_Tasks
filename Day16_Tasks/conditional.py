Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
... import matplotlib.pyplot as plt
... 
... scores = np.array([40, 60, 80, 30, 90])
... 
... pass_count = np.sum(scores > 50)
... fail_count = np.sum(scores <= 50)
... 
... counts = [pass_count, fail_count]
... labels = ["Pass", "Fail"]
... 
... plt.pie(counts, labels=labels, autopct='%1.1f%%')
... plt.title("Pass vs Fail")
