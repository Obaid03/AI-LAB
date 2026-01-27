dict ={}
for i in range(3):
  name=input("Enter Name: ")
  Marks=int(input("Enter Marks: "))
  dict[name]=Marks
print("Student Records: ")
for name,marks in dict.items():
  print(name," : ",marks)
