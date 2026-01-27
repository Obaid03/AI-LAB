name = input("Enter your Name: ")
marks = int(input("Enter Your Marks: "))
print("Name: ", name)
print("Marks: ", marks)
if marks >=85 and marks <=100:
  print("Grade: A")
elif marks >=70 and marks <85:
  print("Grade: B")
elif marks >=50 and marks <70:
  print("Grade: C")
else:
  print("Fail")
