import numpy as np
marks=np.array([[70,80,90],
               [0,75,85],
               [50,65,70],
               [90,95,85],
               [40,55,60]])
total_marks=np.sum(marks,axis=1)
avg_total=np.mean(total_marks)
above_avg_marks=total_marks[total_marks>avg_total]
print("Total marks:",total_marks)
print("Class Average:",avg_total)
print("Above average students:",above_avg_marks)
