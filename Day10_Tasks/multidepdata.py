from numpy import *

BranchA=array([[10,20],[30,40]])
BranchB=array([[5,15],[25,35]])

#branch=concatenate((BranchA,BranchB))
branch=BranchA+BranchB
total_emp=branch.sum()
print("Combined matrix:\n",branch)
print("Total employess across all departments:",total_emp)
