def calculate_average(marks):
  avg=0
  for mark in marks:
    avg+=mark
  return avg/len(marks)

n=int(input("Enter Number of Marks: "))
marks=[]
for i in range(n):
  mark=int(input("Enter Marks : "))
  marks.append(mark)
avg=calculate_average(marks)
print("Marks: ",marks)
print("Average Marks: ",avg)
