import math
students=[("nikky",90),("Abi",60),("Amith",35),("SV",70),("Hemanth",49)]
#ductionary:
dic=dict(students)
# print("Dicionary: \n",dic)

#>50
above50=[]
for names,marks in dic.items():
    if marks>50:
        # print("students >50: \n",names,marks)
        above50.append((names,marks))
marks_list=list(dic.values())
# print(marks_list)
average=math.fsum(marks_list)/len(marks_list)
# print("Average of Marks: \n",average)

#text file
with open("student_Result.txt","w") as file:
    file.write("Students Dictionary: \n")
    file.write(str(dic)+"\n")
    file.write("Above 50: \n")
    file.write(str(above50)+"\n")
    file.write("Average: \n")
    file.write(str(average))
