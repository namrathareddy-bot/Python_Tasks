import copy
employee=[[101,"A"],
          [102,"B"],
          [103,"C"]]
shallow_copy=copy.copy(employee)
#modify 
employee[0][1]="Z"
print("original",employee)
print("modified shallow copy",shallow_copy)


#deep copy
import copy
employee=[[101,"A"],
          [102,"B"],
          [103,"C"]]
deep_copy=copy.deepcopy(employee)
#modify
employee[0][1]="z"
print("Original",employee)
print("modified deep copy",deep_copy)
