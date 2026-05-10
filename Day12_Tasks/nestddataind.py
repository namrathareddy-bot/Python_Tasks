import copy
classes = [["Math", [30, 35]], ["Science", [25, 28]]]
dcopy=copy.deepcopy(classes)
classes[0][1][1]=40
classes[0][1][0]=50
print("Modified: ",classes)
print("Deep Copy (unchanged): ",dcopy)
